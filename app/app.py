import os

import flask
from flask import request, send_from_directory

from app.functions import get_lyrics, transform_to_technical_prose

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


@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

