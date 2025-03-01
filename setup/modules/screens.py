from rich.console import Console
from rich.table import Table
from constants.packages import DESKTOP_ENVIRONMENTS
from constants.enums import DE, DESKTOP_ENVIRONMENT_DICT
from rich.text import Text


console = Console()


def getDETable():
    table = Table(title="Select a Desktop Environment")

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")
    table.add_column("Packages to Install", justify="left", style="green")

    for de in DESKTOP_ENVIRONMENTS:
        table.add_row(de.name.value, de.description, "")
        for pak in de.packages:
            table.add_row("", "", pak.name)

        table.add_row(end_section=True)

    return table


def getPackagesTable(selectedDE):
    print("\n\n")
    if selectedDE == DE.NONE.value:
        noneSelectedText = Text("No packages will be installed")
        noneSelectedText.stylize("bold red")
        console.print(noneSelectedText)
        return
    elif selectedDE in {DE.GNOME.value, DE.HYPRLAND.value, DE.XFCE.value}:
        table = Table(title="Packages for ")

        table.add_column("Name", justify="right", style="cyan", no_wrap=True)
        table.add_column("Description", style="magenta")

        packages = DESKTOP_ENVIRONMENT_DICT[DE(selectedDE)].packages
        for pak in packages:
            table.add_row(pak.name, pak.description)

        table.add_row(end_section=True)

        console.print(table)
        return
