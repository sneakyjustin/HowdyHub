from flask import Flask, render_template, url_for
import json


app = Flask(__name__)


f = open("dummy.json")

all_courses = json.load(f)

f.close()

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/course")
def course():
    return render_template('course.html', posts = all_courses["classes"], title = 'Course')



if __name__ == '__main__':
    app.run(debug=True)
