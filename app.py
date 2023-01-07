from boggle import Boggle
from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = False

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route("/")
def root():
    """root."""
    return redirect("/game")

@app.route("/game")
def show_game():
    """Game."""
    board = boggle_game.make_board()
    return render_template("game.html",board=board)
