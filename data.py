import sqlite3
from movie import Movie
from character import Character
from actor import Actor
from sqlite3 import Error
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_db_file = os.path.join(BASE_DIR, "MovieDB.db")

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_connection():
    """ create a database connection to a SQLite database """
    """ If the db does not exist, it is created for you """
    cn = None
    try:
        cn = sqlite3.connect(_db_file)
    except Error as e:
        print(e)
    return cn

def execute_select(sql_statement: str, data_tuple:tuple=None):
    try:
        cn = create_connection()
        cn.row_factory = sqlite3.Row
        cur = cn.cursor()
        if(data_tuple == None):
            cur.execute(sql_statement)
        else:
            cur.execute(sql_statement, data_tuple)
    except Error as e:
        print(e)
    finally:
        return cur.fetchall()

def execute_insert(sql_statement: str, data_tuple: tuple) -> int:
    last_row_id = 0
    cn = create_connection()
    cur = cn.cursor()
    try:
        cur.execute(sql_statement, data_tuple)
        last_row_id = cur.lastrowid
        cn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()
        cn.close()
        return last_row_id

def get_all_movies() -> []:
    sql_statement = "SELECT * FROM movies"
    rows = execute_select(sql_statement)
    rollodex = []
    for r in rows:
        rollodex.append(Movie.from_SQLiteRow(r))
    return rollodex

def get_all_characters() -> []:
    sql_statement = "SELECT * FROM characters"
    rows = execute_select(sql_statement)
    rollodex = []
    for r in rows:
        rollodex.append(Character.from_SQLiteRow(r))
    return rollodex

def get_all_actors() -> []:
    sql_statement = "SELECT * FROM actors"
    rows = execute_select(sql_statement)
    rollodex = []
    for r in rows:
        rollodex.append(Actor.from_SQLiteRow(r))
    return rollodex

def check_movies_exist(movie_name) -> bool:
    sql_statement = ("Select * from movies where title = ?")
    rows = execute_select(sql_statement, (movie_name,))
    rollodex = []
    for r in rows:
        rollodex.append(Movie.from_SQLiteRow(r))
    if len(rollodex) > 0:
        return True
    else: 
        return False

def check_character_exist(character_name) -> bool:
    sql_statement = ("Select * from characters where name = ?")
    rows = execute_select(sql_statement, (character_name,))
    rollodex = []
    for r in rows:
        rollodex.append(Character.from_SQLiteRow(r))
    if len(rollodex) > 0:
        return True
    else: 
        return False

def check_actor_exist(actor_name) -> bool:
    sql_statement = ("Select * from actors where name = ?")
    rows = execute_select(sql_statement, (actor_name,))
    rollodex = []
    for r in rows:
        rollodex.append(Actor.from_SQLiteRow(r))
    if len(rollodex) > 0:
        return True
    else: 
        return False

def create_movie(new_movie: Movie) -> int:
    insert_statement = "INSERT INTO movies (title) VALUES (?)"
    data_tuple = (new_movie.title,)

    movie_id = execute_insert(insert_statement, data_tuple)
    return movie_id

def create_character(new_character: Character) -> int:
    insert_statement = "INSERT INTO characters (name, movieid) VALUES (?, ?)"
    data_tuple = (new_character.name, new_character.movieid)

    character_id = execute_insert(insert_statement, data_tuple)
    return character_id

def create_actor(new_actor: Actor) -> int:
    insert_statement = "INSERT INTO actors (name, characterid) VALUES (?, ?)"
    data_tuple = (new_actor.name, new_actor.characterid)

    actor_id = execute_insert(insert_statement, data_tuple)
    return actor_id