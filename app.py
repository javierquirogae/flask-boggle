from boggle import Boggle
from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.debug = True

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()
