import os
from flask import Flask, url_for, redirect, render_template, request, session
import logfind


app = Flask(__name__)

app.secret_key = '\x00\x81\xae\x1e[\xdb\xcf\x94\x91\xb8Th\xf5\xea\\\x0e\xfcu\xfa\x8f\x8bE\xe3\xde'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # word_list = request.form['searchfield']
        session['search'] = logfind.search_string("int")
        return redirect(url_for(("results")))
    return render_template("home.html")

@app.route("/results")
def results():
    if 'search' in session:
        results = session['search']
    else:
        session['search'] = "these are the results"
        results = session['search']
    return render_template("results.html", results=results)

@app.route("/results/file=<filename>")
def results_textfile(filename="r.txt"):
    if os.path.exists(filename):
        with open(filename) as f:
            show_file = f.readlines()
    else:
        show_file = "the file content"
    return render_template("showfile.html", show_file=show_file)

if __name__ == "__main__":
    app.run(debug=True)
