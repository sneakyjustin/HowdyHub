from flask import Flask, render_template, url_for, request
import json


app = Flask(__name__)

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/course")
def course_search_list():
    req_dep = request.args.get("dep")
    if req_dep is not None:
        req_dep = req_dep.upper()
    req_course = request.args.get("crs_num")
    req_instr = request.args.get("instr")
    if req_instr is not None:
        req_instr = req_instr.capitalize()
    f = open("dummy.json")
    all_courses = json.load(f)
    f.close()

    courses = []
    for i in all_courses["classes"]:
        if (req_dep is None or i["department"] == req_dep):
            if (req_course is None or i["course"] == req_course):
                if (req_instr is None or i["instructor"] == req_instr):
                    courses.append(i)

    return render_template('course.html', posts = courses, title = 'Course')



if __name__ == '__main__':
    app.run(debug=True)
