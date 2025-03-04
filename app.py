import flask
from flask import request

from main import get_lyrics, transform_to_technical_prose

app = flask.Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return flask.render_template("index.html", title="Home")

@app.route("/lyrics", methods=['POST','GET'])
def lyrics():
	title = request.form["title"]
	artist = request.form["artist"]
	mode = request.form["mode"]

	lyrics = get_lyrics(artist, title)

	transformed_lyrics = transform_to_technical_prose(lyrics, mode)

	return flask.render_template("lyrics.html", lyrics=lyrics, transformed_lyrics=transformed_lyrics, title="Lyrics")