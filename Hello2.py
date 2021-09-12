from flask import Flask, render_template, url_for, request
import json


app = Flask(__name__, static_url_path='/static')

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/course")
def course_search_list():
    req_dep = request.args.get("Department")
    req_course = request.args.get("Course")
    req_instr = request.args.get("Instructor")
    if req_instr is not None:
        req_instr = req_instr.capitalize()
    f = open("dummy.json")
    all_courses = json.load(f)
    f.close()

    courses = []

    for i in all_courses["classes"]:
        if (req_dep=="" or i["department"] == req_dep):
            if (req_course=="" or i["course"] == req_course):
                if (req_instr is None or req_instr=="" or i["instructor"] == req_instr):
                    full_crs_name = i["department"] + " " + i["course"]
                    tmp_class_dict = {
                        "crs_name": full_crs_name,
                        "yr_term": i["term"] + " '" + str(i["year"]),
                        "title": full_crs_name + "-" + i["section"] + " " + i["instructor"],
                        "link": i["link"]
                    }
                    courses.append(tmp_class_dict)

    if len(courses) == 0:
        tmp_class_dict = {
            "crs_name":"",
            "yr_term":"Please refine your search",
            "title":"No classes found",
            "link":"https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"
        }
        courses.append(tmp_class_dict)

    return render_template('course.html', posts = courses, title = 'Course')



if __name__ == '__main__':
    app.run(debug=True)

#TODO No classes found shows "visit groupme"
#TODO Classes change color when hover
#TODO Add footer if time
