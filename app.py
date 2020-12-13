from movie import Movie
import sqlite3
from character import Character
from actor import Actor
from flask import Flask, render_template, request, redirect, url_for, session
from flask import flash
import data
cn = sqlite3.connect("MovieDB.db")
cursor = cn.cursor()
from sqlite3 import Error
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all_movies')
def list_all_movies():
   movies = data.get_all_movies()
   records = len(movies)
   title="Movies"
   print(len(movies))
   return render_template("movie.html", movies = movies)

@app.route('/all_characters')
def list_all_characters():
    characters = data.get_all_characters()
    records = len(characters)
    title="Characters"
    print(len(characters))
    return render_template("character.html", characters = characters)

@app.route('/all_actors')
def list_all_actors():
   actors = data.get_all_actors()
   records = len(actors)
   title="Actors"
   print(len(actors))
   return render_template("actor.html", actors = actors)

@app.route('/movie_form')
def movie_form():
   return render_template("movie_form.html")

@app.route('/character_form')
def character_form():
    return render_template("character_form.html")

@app.route('/actor_form')
def actor_form():
    return render_template("actor_form.html")

@app.route('/check_movie', methods = ['POST'])
def check_movie():
    movie_name = request.form['movie_name']
    if data.check_movies_exist(movie_name) == True:
        print("check this")
        flash('Movie already exists in database')
        return redirect(url_for('movie_form'))
    else:
        print("check that")
        movie_name = request.form['movie_name']     
        print(f"Movie Name: {movie_name}")
        movie = Movie()
        print(f"Movie ID: {movie.movieid}")
        movie.title = movie_name
        data.create_movie(movie)
        return redirect(url_for('list_all_movies'))

@app.route('/check_character', methods = ['POST'])
def check_character():
    character_name = request.form['character_name']
    print(character_name)
    if data.check_character_exist(character_name) == True:
        print("check this")
        flash('Character already exists in database')
        return redirect(url_for('character_form'))
    else:
        print("check that")
        character_name = request.form['character_name']
        character_movie_id = request.form['character_movieid']     
        print(f"Character Name: {character_name}")
        print(f"Movie ID: {character_movie_id}")
        new_character = Character()
        new_character.name = character_name
        new_character.movieid = character_movie_id
        data.create_character(new_character)
        return redirect(url_for('list_all_characters'))

@app.route('/check_actor', methods = ['POST'])
def check_actor():
    actor_name = request.form['actor_name']
    print(actor_name)
    if data.check_actor_exist(actor_name) == True:
        print("check this")
        flash('Actor already exists in database')
        return redirect(url_for('actor_form'))
    else:
        print("check that")
        actor_name = request.form['actor_name']
        actor_character_id = request.form['characterid']     
        print(f"Actor Name: {actor_name}")
        print(f"Character ID: {actor_character_id}")
        new_actor = Actor()
        new_actor.name = actor_name
        new_actor.characterid = actor_character_id
        data.create_actor(new_actor)
        return redirect(url_for('list_all_actors'))

@app.route('/new_movie', methods = ['POST'])
def new_movie_form():  
   movie_name = request.form['movie_name']     
   print(f"Movie Name: {movie_name}")
   movie = Movie()
   print(f"Movie ID: {movie.movieid}")
   movie.title = movie_name
   data.create_movie(movie)
   return redirect(url_for('list_all_movies'))

@app.route('/new_character', methods = ['POST'])
def new_character_form():  
   character_name = request.form['character_name']
   print("Hello World")
   movieid = request.form['character_movieid']
   character_movie_id = session.get('character_movieid')
   print(f"Character Name: {character_name}")
   print(f"Movie ID: {character_movie_id}")
   character = Character()
   character.name = character_name
   character.movieid = character_movie_id
   data.create_character(character)
   return redirect(url_for('list_all_characters'))

@app.route('/new_actor', methods = ['POST'])
def new_actor_form():  
   actor_name = request.form['actor_name']
   characterid = request.form['characterid']
   #character_movie_id = session.get('movieid')
   print(f"Actor Name: {actor_name}")
   #print(f"Actor ID: {actorid}")
   actor = Actor()
   actor.name = actor_name
   actor.characterid = characterid
   data.create_actor(actor)
   return redirect(url_for('list_all_actors'))


if __name__ == '__main__':
   app.secret_key = "23123DJFdkjafjq29ygd873y4"
   app.run(debug=True)