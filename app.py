from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hackathonHavoc")
def about():
    return render_template("hackathonHavoc.html")

if __name__ == "__main__":
    app.run(debug=True)