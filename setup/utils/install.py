import subprocess


def install_packages(packages):
    for pak in packages:
        subprocess.run(
            ["yay", "-S", "--noconfirm", pak.name],
        )
