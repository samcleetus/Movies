import sqlite3


class Rating():
    def __init__(self):
        super().__init__()
        self.ratingid = ratingid
        self.rating = rating

    def to_dict(self) -> {}:
        return self.__dict__

    def __str__(self):
        return f"Rating ID:{self.ratingid}; Rating: {self.rating}"

    @classmethod
    def from_title(cls, rating) -> 'Rating':
        c = Rating()
        c.rating = rating
        return c

    @classmethod
    def from_dict(cls, row: dict) -> 'Rating':
        c = Rating()
        c.ratingid = row['ratingid']
        c.rating = row['rating']
        return c

    @classmethod
    def from_SQLiteRow(cls, row: sqlite3.Row) -> 'Rating':
        a = Rating()
        a.ratingid = row['ratingid']
        a.rating = row['rating']
        return a