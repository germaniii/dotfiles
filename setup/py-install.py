from rich.console import Console
from rich.table import Table
from constants.packages import DESKTOP_ENVIRONMENTS
from modules.screens import getDETable

table = getDETable()

console = Console()
console.print(table)
