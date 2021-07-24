"""
Main application file for importing all required model classes and geting work done here
"""
# Internal imports
from View.UserMessagesView import UserMessagesView
from View.WorkTableView import WorkTableView
from View.TasksTableView import TaskTableView
from View.Resources.ApplicationStrings import (
    MainApplicationStrings,
    TasksInstructionStrings,
    UserMessagesStrings,
    ExceptionStrings,
    WorkInstructionStrings,
)
from View.Resources.LayoutInformation import LayoutNames, LayoutStyles
from View.InstructionsView import InstructionsView

# External imports

# External UI imports
from rich.table import Table
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel


class TasknWork:
    def MakeBaseLayout(self):
        """
        Function to set base layout of application
        """
        self.layout = Layout(name=LayoutNames.Root)

        self.layout.split(
            Layout(name=LayoutNames.Margin, size=1),
            Layout(name=LayoutNames.Header, size=3),
            Layout(name=LayoutNames.Main, ratio=1),
            Layout(name=LayoutNames.Footer, size=7),
        )
        self.layout[LayoutNames.Main].split_row(
            Layout(name=LayoutNames.Side),
            Layout(name=LayoutNames.Body, ratio=3, minimum_size=60),
        )

        self.layout[LayoutNames.Side].split(
            Layout(name=LayoutNames.Box11), Layout(name=LayoutNames.Box21)
        )

        self.layout[LayoutNames.Body].split(
            Layout(name=LayoutNames.Box12), Layout(name=LayoutNames.Box22)
        )

        self.userMessageView = UserMessagesView(self.layout[LayoutNames.Footer])

    def PopulateLayouts(self):
        self.layout[LayoutNames.Header].update(
            self.CreateHeader(),
        )

    def CreateHeader(self) -> Panel:
        """Display header with clock."""
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row(f"[b]{MainApplicationStrings.ApplicationTitle}[/b]")
        return Panel(grid, style=LayoutStyles.Title)

    def WorkInstructions(self):
        instructions = InstructionsView()
        self.layout[LayoutNames.Box11].update(
            instructions.CreateInstructions(WorkInstructionStrings.Options)
        )

    def WorksTableView(self):
        self.workView = WorkTableView(self.userMessageView)
        self.layout[LayoutNames.Box12].update(self.workView.CreateWorkView())

    def TaskInstructions(self):
        instructions = InstructionsView()
        self.layout[LayoutNames.Box21].update(
            instructions.CreateInstructions(TasksInstructionStrings.Options)
        )

    def TasksTableView(self):
        self.tableView = TaskTableView()
        self.layout[LayoutNames.Box22].update(self.tableView.CreateTasksView())

    def MainLoop(self, console):
        isContinue = True
        while isContinue:
            console.print(self.layout)
            opt = console.input()
            if opt == "1":
                # Create work
                task = console.input("Create work : ")
                category = console.input("category : ")
                self.workView.CreateWork(task, category)
            elif opt == "2":
                workID = int(console.input("ID to update : "))
                work = self.workView.GetWorkByID(workID)
                work.description = console.input(f"Current description : {work.description} : ")
                self.workView.UpdateWork(work)
            elif len(opt) > 3:
                isContinue = False

    def MainFunction(self):
        """Function with main application loop"""
        self.MakeBaseLayout()
        self.PopulateLayouts()
        self.WorkInstructions()
        self.TaskInstructions()
        self.WorksTableView()
        self.TasksTableView()
        console = Console()
        self.MainLoop(console)
