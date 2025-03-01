from rich.table import Table
from constants.packages import DESKTOP_ENVIRONMENTS


def getDETable():
    table = Table(title="Select a Desktop Environment")

    table.add_column("Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")
    table.add_column("Packages to Install", justify="left", style="green")

    for de in DESKTOP_ENVIRONMENTS:
        table.add_row(de.name.value, de.description, de.packages[0].name)
        for pak in de.packages[1:]:
            table.add_row("", "", pak.name)

        table.add_row(end_section=True)

    return table
