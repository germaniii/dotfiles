import asyncio
from events.package_installed import PackageInstalled
from textual.widgets import (
    Log,
)


async def install_packages(screen):
    selected_packages = [*screen.desktop_selection, *screen.package_selection]
    progress_text = screen.query_one(
        "#install_processing-progress_text",
        Log,
    )

    for package in selected_packages:
        check_process = await asyncio.create_subprocess_exec(
            "yay",
            "-Si",
            package,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        await check_process.communicate()
        if check_process.returncode != 0:
            progress_text.write_line("Package not found: " + package)
            screen.post_message(PackageInstalled(package=package, is_success=False))
            continue

        install_process = await asyncio.create_subprocess_exec(
            "yay",
            "-S",
            "--noconfirm",
            package,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        async def read_stream(stream, prefix):
            """Read the stream line by line and append output to progress_text."""
            while True:
                line = await stream.readline()
                if not line:
                    break  # End of stream

                progress_text.write_line(f"{prefix} {line.decode().strip()}")

        # Read stdout and stderr concurrently
        await asyncio.gather(
            read_stream(install_process.stdout, "[stdout]"),
            read_stream(install_process.stderr, "[stderr]"),
        )

        if check_process.returncode != 0:
            progress_text.write_line("Failed to install: " + package)
            screen.post_message(PackageInstalled(package=package, is_success=False))
        else:
            progress_text.write_line("Successfully Installed " + package)
            screen.post_message(PackageInstalled(package=package, is_success=True))

        screen.refresh()  # Ensure UI updates
