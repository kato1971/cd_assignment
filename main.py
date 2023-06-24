from flask import Flask, render_template, redirect

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title = "Index")

@app.route("/home")
def home():
    return redirect("/", code=302 )

@app.route("/about")
def about():
    return render_template("about.html", title = "About")