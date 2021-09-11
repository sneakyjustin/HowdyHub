from flask import Flask, render_template, url_for



app = Flask(__name__)

posts = [
    {
        'Course' : 'Course Name/Number',
        'Professor' : 'Professor Name',
        'GroupMe' : 'Link to GroupMe',
        'Semester' : 'Semester and Year'
    },

    {
        'Course' : 'Course Name/Number',
        'Professor' : 'Professor Name',
        'GroupMe' : 'Link to GroupMe',
        'Semester' : 'Semester and Year'
    }

]  

@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/course")
def course():
    return render_template('course.html', posts = posts, title = 'Course')



if __name__ == '__main__':
    app.run(debug=True)
