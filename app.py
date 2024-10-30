import string
from flask import Flask, render_template
from pathlib import Path

import recipe
from recipe import Recipe

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    recipes = recipe.recipes_list()
    return render_template("index.html", recipes=recipes, title="Home Page")


@app.route("/ping")
def ping():
    return "200"


@app.route("/p/<slug>")
def blog_post(slug):
    this_recipe = Recipe(slug)
    return render_template("generated/" + slug + ".html", title=this_recipe.title)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
