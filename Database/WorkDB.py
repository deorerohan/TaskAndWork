import sqlite3
import datetime

class WorkDB:
    def __init__(self) -> None:
        self.connect = sqlite3.connect("WorkDatabase.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            "create table if not exists WorkDB(description text, category text, creationDate date) "
        )

    def AddWork(self, work):
        self.cursor.execute(
            "insert into WorkDB(description, category, creationDate) values(?, ?, ?)",
            (work.description, work.category, work.creationDate),
        )
        return self.cursor.lastrowid

    def ReadAllWork(self):
        today = str(datetime.date.today())
        return self.cursor.execute(f'select rowid, * from WorkDB where creationDate like "{today}%"').fetchall()

    def UpdateWork(self, work):
        # Function to update work in database
        self.cursor.execute(f'update WorkDB set description="{work.description}", category={work.category} where rowid = {work.workID}')
    
    def __del__(self):
        self.connect.commit()
        self.connect.close()
