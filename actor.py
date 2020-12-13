import sqlite3


class Actor():
    def __init__(self):
        super().__init__()
        self.actorid = ""
        self.characterid = ""
        self.name = ""

    def to_dict(self) -> {}:
        return self.__dict__

    def __str__(self):
        return f"Actor Name:{self.name}; Actor ID; {self.actorid} Character ID: {self.characterid}"

    @classmethod
    def from_title(cls, fname) -> 'Actor':
        a = Actor()
        a.name = name
        return a

    @classmethod
    def from_dict(cls, row: dict) -> 'Actor':
        a = Actor()
        a.actorid = row['actorid']
        a.characterid = row['characterid']
        a.name = row['name']
        return a

    @classmethod
    def from_SQLiteRow(cls, row: sqlite3.Row) -> 'Actor':
        a = Actor()
        a.actorid = row['actorid']
        a.characterid = row['characterid']
        a.name = row['name']
        return a