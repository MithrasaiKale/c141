from flask import Flask, jsonify, request
import csv 

all_movies=[]

with open("movies.csv") as movie:
    movie1=csv.reader(movie)
    a = list(movie1)
    all_movies=a[1:]
    
liked_movies=[]
disliked_movies=[]
not_viewed_movies=[]

app=Flask(__name__)

@app.route("/")
def flask1():
    return "Welcome"

@app.route("/get-movie")
def get_movie():
    return jsonify({
    "data" : all_movies[0], "status" : "success"
    })

@app.route("/liked-movies", methods=["POST"])
def liked_movies():
    global all_movies
    m=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(m)
    return jsonify({
        "status" : "success"
    }),200
    
@app.route("/disliked-movies", methods=["POST"])
def disliked_movies():
    global all_movies
    m=all_movies[0]
    all_movies=all_movies[1:]
    disliked_movies.append(m)
    return jsonify({
        "status" : "success"
    }),200

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch_movies():
    global all_movies
    m=all_movies[0]
    all_movies=all_movies[1:]
    not_viewed_movies.append(m)
    return jsonify({
        "status" : "success"
    }),200
    
if (__name__ == "__main__"):
    app.run(debug=True)