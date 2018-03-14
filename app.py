#import Flask & its dependencies
from flask import Flask
from flask import render_template, request, make_response, redirect, url_for

#import other packages
import os
import json
from datetime import datetime

#instantiating a flask app
app = Flask(__name__)
month_names = ['Jan', 'Feb', 'Mar','May','Jun','Jul','Aug', 'Sep','Oct','Nov','Dec']

def read_highlights():
    highlights_data = json.load(open('static/json/highlights.json'))
    return highlights_data

def read_people_status():
    status_data = json.load(open('static/json/people-status.json'))
    for entry in status_data.values():
        print entry
    return status_data

@app.route("/")
def main():
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    print currentMonth
    final_data = {}
    highlights = read_highlights()
    data = highlights[str(currentYear)][month_names[currentMonth-1]]
    final_data["highlights"]=data

    final_data["statuses"] = read_people_status()
    print final_data
    return render_template('index.html', data = final_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
