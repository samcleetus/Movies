import sqlite3


class Description():
    def __init__(self):
        super().__init__()
        self.description_id = ""
        self.description = ""
        self.movieid = ""

    def to_dict(self) -> {}:
        return self.__dict__

    def __str__(self):
        return f"Description ID:{self.description_id}; Movie ID: {self.movieid}"

    @classmethod
    def from_title(cls, description) -> 'Description':
        c = Description()
        c.description = description
        return c

    @classmethod
    def from_dict(cls, row: dict) -> 'Description':
        c = Description()
        c.description_id = row['description_id']
        c.description = row['description']
        c.movieid = row['movieid']
        return c

    @classmethod
    def from_SQLiteRow(cls, row: sqlite3.Row) -> 'Description':
        a = Description()
        a.id = row['id']
        a.description = row['description']
        a.movieid = row['movieid']
        return a