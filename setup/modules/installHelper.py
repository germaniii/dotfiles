from constants.enums import DESKTOP_ENVIRONMENT_DICT
import subprocess
import getpass


def installDEPackages(selectedDE):
    packages = DESKTOP_ENVIRONMENT_DICT[selectedDE].packages
    # ask for user password before proceeding
    getpass.getpass()

    for pak in packages:
        subprocess.run(
            ["yay", "-S", "--noconfirm", pak.name],
        )
