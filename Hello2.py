from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

f = open("dummy.json")

posts = json.load(f)

f.close()

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', posts = posts["classes"], title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)