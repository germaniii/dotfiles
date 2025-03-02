from rich.console import Console
from rich.table import Table
from constants.packages import DESKTOP_ENVIRONMENTS
from constants.enums import DE, DESKTOP_ENVIRONMENT_DICT
from rich.text import Text


console = Console()


def print_desktop_environment_table():
    table = Table(title="Select a Desktop Environment")

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")
    table.add_column("Packages to Install", justify="left", style="green")

    for de in DESKTOP_ENVIRONMENTS:
        table.add_row(de.name.value, de.description, "")
        for pak in de.packages:
            table.add_row("", "", pak.name)

        table.add_row(end_section=True)

    console.print(table)
    return


def print_de_packages_table(selected_de):
    print("\n")
    match selected_de:
        case DE.NONE:
            noneSelectedText = Text("No packages will be installed")
            noneSelectedText.stylize("bold red")
            console.print(noneSelectedText)
            return
        case DE.GNOME | DE.HYPRLAND | DE.XFCE:
            packages = DESKTOP_ENVIRONMENT_DICT[selected_de].packages
            print_packages_table(selected_de.value, packages)
            return


def print_packages_table(title, packages, caption=""):
    print("\n")
    table = Table(title=title, caption=caption)

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")

    for pak in packages:
        table.add_row(pak.name, pak.description)

    table.add_row(end_section=True)

    console.print(table)
    return
