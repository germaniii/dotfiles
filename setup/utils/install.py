import subprocess


def install_package(package):
    f = open("yay-logs.txt", "a")
    subprocess.run(
        ["yay", "-S", "--noconfirm", package.name],
        check=True,
        stdout=f,
        stderr=subprocess.STDOUT,
    )
