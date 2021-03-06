from movie import Movie
import sqlite3
from character import Character
from description import Description
from actor import Actor
from flask import Flask, render_template, request, redirect, url_for, session
from flask import flash
import data
cn = sqlite3.connect("MovieDB.db")
cursor = cn.cursor()
from sqlite3 import Error
app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/all_movies')
def list_all_movies():
    movies = data.get_all_movies()
    records = len(movies)
    title="Movies"
    print(len(movies))
    return render_template("movie.html", movies = movies, path=request.path)

@app.route('/all_characters')
def list_all_characters():
    characters = data.get_all_characters()
    records = len(characters)
    title="Characters"
    print(len(characters))
    return render_template("character.html", characters = characters, path=request.path)

@app.route('/all_actors')
def list_all_actors():
   actors = data.get_all_actors()
   records = len(actors)
   title="Actors"
   print(len(actors))
   return render_template("actor.html", actors = actors, path=request.path)

@app.route('/movie_form')
def movie_form():
   return render_template("movie_form.html")

@app.route('/character_form')
def character_form():
    movies = data.get_all_movies()
    return render_template("character_form.html", movies = movies)

@app.route('/actor_form')
def actor_form():
    return render_template("actor_form.html")

@app.route('/description_form')
def description_form():
    return render_template("description_form.html")

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


app.route('/check_desc', methods = ['POST'])
def check_desc():
    movie_id = request.form['description_movieid']
    print(movie_id)
    if data.check_description_exist(movie_id) == True:
        print("check this")
        flash('This movie already has a description')
        return redirect(url_for('description_form'))
    else:
        print("check that")
        movie_id = request.form['description_movieid']
        description = request.form['description']     
        #print(f"Actor Name: {actor_name}")
        print(f"Movie ID: {movie_id}")
        new_description = Actor()
        new_description.description = description
        new_description.movieid = movieid
        data.create_description(new_description)
        flash('Movie description successfully added')
        return redirect(url_for('list_all_movies'))


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

@app.route('/new_description', methods = ['POST'])
def new_description_form():
    movie_id = request.form['description_movieid']
    description = request.form['description']     
    print(f"Movie ID: {movie_id}")
    new_description = Description()
    new_description.description = description
    new_description.movieid = movie_id
    data.create_description(new_description)
    return redirect(url_for('list_all_movies'))

#@app.route('/search_movie', methods = ['POST'])
#def search_movie():
    #movies = data.get_all_movies
    #search_movie_name = request.form['search_movie']
    #if data.search_movie(search_movie_name) == True:

@app.route('/delete_movie/<movie_id>', methods=['GET'])
def delete_movie(movie_id):
    #movie_id = request.form['movie_id']
    print(movie_id)
    if data.delete_movie(movie_id) == True:
        flash('Item deleted from database')
        return redirect(url_for('list_all_movies'))
    else:
        flash("Action was unsuccessful")

@app.route('/delete_character/<character_id>', methods=['GET'])
def delete_character(character_id):
    print(character_id)
    if data.delete_character(character_id) == True:
        flash('Item deleted from database')
        return redirect(url_for('list_all_characters'))
    else:
        flash("Action was unsuccessful")

@app.route('/delete_actor/<actor_id>', methods=['GET'])
def delete_actor(actor_id):
    print(actor_id)
    if data.delete_actor(actor_id) == True:
        flash('Item deleted from database')
        return redirect(url_for('list_all_actors'))
    else:
        flash("Action was unsuccessful")

@app.route('/get_description/<movie_id>', methods = ['GET'])
def get_description(movie_id):
    print(movie_id)
    descriptions = data.get_description(movie_id)
    return render_template("description.html", descriptions = descriptions)

@app.route('/search_movie', methods = ['POST'])
def search_movie():
    movie_name = request.form['name']
    movies = data.get_movie(movie_name)
    flash("Movies found!")
    return render_template("search_movie.html", movies = movies)

@app.route('/search_character', methods = ['POST'])
def search_character():
    character_name = request.form['name']
    characters = data.get_character(character_name)
    flash("Characters found!")
    return render_template("search_character.html", characters = characters)

@app.route('/search_actor', methods = ['POST'])
def search_actor():
    actor_name = request.form['name']
    actors = data.get_actor(actor_name)
    flash("Actors found!")
    return render_template("search_actor.html", actors = actors)

if __name__ == '__main__':
   app.secret_key = "23123DJFdkjafjq29ygd873y4"
   app.run(debug=True)