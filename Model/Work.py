from Database.WorkDB import WorkDB
import datetime


class Work:
    def __init__(
        self, description, category, id=-1, date=datetime.datetime.today()
    ) -> None:
        self.description = description
        self.category = category
        self.workID = id
        self.creationDate = date

    def SetWorkID(self, id):
        self.workID = id


class WorkTable:
    def __init__(self) -> None:
        self.worksList = list()
        self.db = WorkDB()

    def AddNewWork(self, description, category) -> None:
        self.worksList.append(Work(description, category))
        id = self.db.AddWork(self.worksList[-1])
        self.worksList[-1].SetWorkID(id)

    def ReadAllWork(self) -> None:
        allWork = self.db.ReadAllWork()
        for work in allWork:
            self.worksList.append(Work(work[1], work[2], work[0], work[3]))
