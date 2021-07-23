"""Class for display error messages for short time in footer 
and extra information while it is relevant
"""


from rich.panel import Panel

class UserMessagesView:
    def __init__(self, messageArea) -> None:
        self.messageArea = messageArea

    def RemoveMessage(self):
        self.messageArea.update(Panel(""))

    def ShowUserMessage(self, message):
        self.messageArea.update(Panel(message))

    def ShowErrorMessage(self):
        pass

    def ShowDetailInformation(self):
        pass
