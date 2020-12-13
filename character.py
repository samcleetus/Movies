import sqlite3


class Character():
    def __init__(self):
        super().__init__()
        self.characterid = ""
        self.movieid = ""
        self.name = ""

    def to_dict(self) -> {}:
        return self.__dict__

    def __str__(self):
        return f"Character Name:{self.name}; Character ID; {self.characterid} Movie ID: {self.movieid}"

    @classmethod
    def from_title(cls, fname) -> 'Character':
        c = Character()
        c.name = name
        return c

    @classmethod
    def from_dict(cls, row: dict) -> 'Character':
        c = Character()
        c.characterid['characterid']
        c.movieid = row['movieid']
        c.name = row['name']
        return c

    @classmethod
    def from_SQLiteRow(cls, row: sqlite3.Row) -> 'Character':
        a = Character()
        a.characterid = row['characterid']
        a.movieid = row['movieid']
        a.name = row['name']
        return a