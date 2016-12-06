import os
from flask import Flask, Response, url_for, redirect, render_template, request, session
import logfind


app = Flask(__name__)

app.secret_key = '\x00\x81\xae\x1e[\xdb\xcf\x94\x91\xb8Th\xf5\xea\\\x0e\xfcu\xfa\x8f\x8bE\xe3\xde'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        word_list = request.form['search']
        session['searchfield'] = logfind.search_string(word_list)
        return redirect(url_for(("results")))
    return render_template("home.html")

@app.route("/results/", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        word_list = request.form['search']
        session['searchfield'] = logfind.search_string(word_list)
        return redirect(url_for(("results")))

    if 'searchfield' in session:
        results = session['searchfield']
    return render_template("results.html", results=results)

@app.route("/<file_name>")
def results_textfile(file_name=None):
    def generate_text():
        print(file_name)
        # if os.path.exists(os.path.curdir+"static/text/"+file_name):
        with open(file_name) as f:
            show_file = f.readlines()
            return show_file
    return Response(generate_text(), mimetype="text/txt")


if __name__ == "__main__":
    app.run(debug=True)
