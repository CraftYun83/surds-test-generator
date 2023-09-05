from main import Problems
import os
from flask import Flask, render_template, send_from_directory, make_response

problems = Problems()
app = Flask(__name__)

@app.after_request
def add_header(response):    
  response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
  if ('Cache-Control' not in response.headers):
    response.headers['Cache-Control'] = 'public, max-age=600'
  return response

@app.route("/")
def index():
    response = make_response(render_template("index.html"))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route('/media/<path:filename>')
def send_media(filename):
    response = make_response(send_from_directory("media/",
                               filename))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

@app.route("/deleteMedia/<path:filename>")
def delete_media(filename):
    if ".png" in filename:
        os.remove(os.path.dirname(os.path.abspath(__file__))+"\\media\\problems\\"+filename.split("/")[1])
    return "true"

@app.route('/createProblems', methods=["POST"])
def create_problems():
    return {
        "problems": [
            problems.easySimplify(),
            problems.missingHypotenuse(),
            problems.rationaliseDenominator()
        ]
    }

app.run("0.0.0.0", port=6942)