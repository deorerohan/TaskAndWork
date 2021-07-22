import sqlite3


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
        return self.cursor.execute("select rowid, * from WorkDB").fetchall()

    def __del__(self):
        self.connect.commit()
        self.connect.close()
