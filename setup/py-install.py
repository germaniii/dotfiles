from rich.console import Console
from rich.prompt import Prompt
from constants.enums import DE
from constants.packages import (
    TERMINAL_UTILITIES,
    ESSENTIAL_AUR_PACKAGES,
    ADDITIONAL_THEMING_PACKAGES,
    ADDITIONAL_APPLICATION_PACKAGES,
    DESKTOP_ENVIRONMENT_DICT,
)
from modules.screens import (
    print_desktop_environment_table,
    print_packages_table,
)
from modules.install_helper import (
    confirm_selection,
    install_packages,
)

console = Console()
desktop_environment_packages_confirm = False

package_groups = [
    (
        "Terminal Utility Packages",
        TERMINAL_UTILITIES,
        "to install terminal utilities",
    ),
    (
        "Essential AUR Packages",
        ESSENTIAL_AUR_PACKAGES,
        "to install essential AUR packages",
    ),
    (
        "Theming Packages (optional)",
        ADDITIONAL_THEMING_PACKAGES,
        "to install additional theming packages",
    ),
    (
        "Application Packages (optional)",
        ADDITIONAL_APPLICATION_PACKAGES,
        "to install additional application packages",
    ),
]

confirmed_packages = []


###############################################################################
# Desktop Environements
###############################################################################
while not desktop_environment_packages_confirm:
    table = print_desktop_environment_table()

    selected_de = DE(
        Prompt.ask(
            "Enter your choice",
            choices=[
                DE.GNOME.value,
                DE.XFCE.value,
                DE.HYPRLAND.value,
                DE.NONE.value,
            ],
            default=DE.NONE.value,
        )
    )

    if selected_de != DE.NONE:
        print_packages_table(
            title="Packages from " + selected_de.value,
            packages=DESKTOP_ENVIRONMENT_DICT[selected_de].packages,
        )

    desktop_environment_packages_confirm = confirm_selection(selected_de.value)
    confirmed_packages.append(DESKTOP_ENVIRONMENT_DICT[selected_de].packages)


###############################################################################
#  Applications Install
###############################################################################
for title, package_list, confirmation_message in package_groups:
    print_packages_table(title=title, packages=package_list)
    if confirm_selection(confirmation_message):
        confirmed_packages.append(package_list)

for package_list in confirmed_packages:
    install_packages(package_list)
