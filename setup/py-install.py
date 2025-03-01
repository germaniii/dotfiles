from rich.console import Console
from constants.enums import DE
from modules.screens import getDETable, getPackagesTable
from modules.installHelper import installDEPackages
from rich.prompt import Prompt, Confirm

console = Console()
selectedDEConfirm = False

while not selectedDEConfirm:
    table = getDETable()

    selectedDE = DE(
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

    getPackagesTable(selectedDE)
    selectedDEConfirm = Confirm.ask(
        "Would you like to proceed with " + selectedDE.value + "?", default=True
    )

if selectedDE != DE.NONE:
    installDEPackages(selectedDE)
