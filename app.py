from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Tokyo, Japan',
        'salary': '$40,000'
    },

    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Shanghai, China',
        'salary': '$45,000'
    },


    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': '$35,000'
    },

    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': '$50,000'
    },
]

@app.route("/")
def index():
    return render_template('home.html',
                           jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)