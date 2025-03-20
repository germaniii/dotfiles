import subprocess

from setup.constants.classes import Package


def install_package(package: Package) -> bool:
    f = open("yay-logs.txt", "a")
    try:
        _ = subprocess.run(
            ["yay", "-Si", package.name],
            check=True,
            stdout=f,
            stderr=subprocess.STDOUT,
        )
        _ = subprocess.run(
            ["yay", "-S", "--noconfirm", package.name],
            check=True,
            stdout=f,
            stderr=subprocess.STDOUT,
            text=True,
        )

        return True
    except subprocess.CalledProcessError:
        return False
