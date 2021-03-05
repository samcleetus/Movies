import sqlite3


class Movie():
    def __init__(self):
        super().__init__()
        self.movieid = ""
        self.title = ""
        #self.description = ""

    def to_dict(self) -> {}:
        return self.__dict__

    def __str__(self):
        return f"Movie Title:{self.title}; Movie ID: {self.movieid}"

    @classmethod
    def from_title(cls, fname) -> 'Movie':
        c = Movie()
        c.title = title
        return c

    @classmethod
    def from_dict(cls, row: dict) -> 'Movie':
        c = Movie()
        c.movieid = row['movieid']
        c.title = row['title']
        #c.description = row['description']
        return c

    @classmethod
    def from_SQLiteRow(cls, row: sqlite3.Row) -> 'Movie':
        a = Movie()
        a.movieid = row['movieid']
        a.title = row['title']
        #a.description = row['description']
        return a