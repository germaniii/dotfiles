import subprocess

from setup.constants.classes import Package


def install_package(package: Package):
    # TODO: Add yay -Si <package-name> to check if package is not found
    f = open("yay-logs.txt", "a")
    _ = subprocess.run(
        ["yay", "-S", "--noconfirm", package.name],
        check=True,
        stdout=f,
        stderr=subprocess.STDOUT,
    )
