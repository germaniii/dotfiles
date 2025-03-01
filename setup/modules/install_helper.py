from rich.prompt import Confirm
import subprocess


def install_packages(packages):
    for pak in packages:
        subprocess.run(
            ["yay", "-S", "--noconfirm", pak.name],
        )


def confirm_selection(item=""):
    return Confirm.ask("Are you sure " + item + "?", default=True)
