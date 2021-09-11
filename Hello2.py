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
    return render_template('home.html', posts = posts, title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)