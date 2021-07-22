from rich.table import Table
from rich.panel import Panel


class InstructionsView:
    """Class to display instruction on side bar"""

    def __init__(self) -> None:
        pass

    def CreateInstructions(self, options) -> Panel:
        table = Table(expand=True, show_edge=False)

        table.add_column("Select an option : ", style="cyan", no_wrap=True)

        for op in options:
            table.add_row(op)

        return Panel(table)
