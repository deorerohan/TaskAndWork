"""
Main application file for importing all required model classes and geting work done here
"""
# Internal imports
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

    def TaskInstructions(self):
        instructions = InstructionsView()
        self.layout[LayoutNames.Box21].update(
            instructions.CreateInstructions(TasksInstructionStrings.Options)
        )

    def MainFunction(self):
        """Function with main application loop"""
        self.MakeBaseLayout()
        self.PopulateLayouts()
        self.WorkInstructions()
        self.TaskInstructions()
        console = Console()
        console.print(self.layout)
