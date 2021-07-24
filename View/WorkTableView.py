from View.UserMessagesView import UserMessagesView
from Model.Work import Work, WorkTable

from rich.table import Table
from rich.panel import Panel

import threading

class WorkDetailView:
    def GetWorkDetailView(work) -> Table:
        table = Table(expand=True, show_edge=False)

        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Creation Date", style="magenta")
        table.add_column("Description", style="green")
        table.add_column("Category", style="yellow")
        table.add_row(str(work.workID), work.creationDate, work.description, work.category)
        return table


class WorkTableView:
    def __init__(self, userMessageView) -> None:
        self.WorkController = WorkTable()
        self.userMessageView = userMessageView

    def CreateWorkView(self) -> Panel:
        """Some example content."""
        self.WorkController.ReadAllWork()
        
        self.table = Table(expand=True, show_edge=False)

        self.table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        self.table.add_column("Creation Date", style="magenta")
        self.table.add_column("Description", style="green")
        self.table.add_column("Category", style="yellow")

        for work in self.WorkController.worksList:
            self.table.add_row(str(work.workID), work.creationDate, work.description, work.category)

        return Panel(self.table)

    def CreateWork(self, work, category) -> None:
        workItem = self.WorkController.AddNewWork(work, category)
        self.table.add_row(str(workItem.workID), str(workItem.creationDate), workItem.description, workItem.category)
        self.userMessageView.ShowUserMessage(f"Work created : {work}")
        timer = threading.Timer(5, self.userMessageView.RemoveMessage)
        timer.start()

    def GetWorkByID(self, id) -> Work:
        item = [work for work in self.WorkController.worksList if work.workID == id]
        if len(item) == 1:
            return item[0]
        return None

    def UpdateWork(self, work) -> None:
        self.WorkController.UpdateWork(work)
        # Need to update table for new values
    
    def DisplayWork(self, work) -> None:
        # Function to display complete details about work
        self.userMessageView.ShowUserMessage(WorkDetailView.GetWorkDetailView(work))
        