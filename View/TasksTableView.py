from rich.table import Table
from rich.panel import Panel


class TaskTableView:
    def __init__(self) -> None:
        pass

    def CreateTasksView(self) -> Panel:
        """Some example content."""
        table = Table(title="Star Wars Movies", expand=True, show_edge=False)

        table.add_column("Released", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Box Office", style="green")

        table.add_row(
            "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690"
        )
        table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
        table.add_row(
            "Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889"
        )

        return Panel(table)
