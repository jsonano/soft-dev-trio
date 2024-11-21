# TNPG: Abacus
# Roster: Jason Chao and Leon Huang
# SoftDev
# K23 - Rest APIs
# 11-21-24
# Time spent: 1

from flask import Flask, render_template

import requests
from urllib import request
import json

app = Flask(__name__)

@app.route('/')
def rest_api():
    with open('key_nasa.txt') as f:
        api_key = f.read().strip()

    api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    # with request.urlopen(api_url) as response:
    #     html = response.read()

    # print(requests.get(api_url)) # prints out the response code
    json_data = requests.get(api_url).json() # prints out all data in JSON tab of console
    # print(requests.get(api_url).json())

    # print(json.dumps(json_data, sort_keys=True, indent=4)) # prints out the data in a more readable format
    python_data = json.loads(json.dumps(json_data, sort_keys=True, indent=4)) # converts the JSON data into a Python dictionary
    # print(python_data)

    return render_template('main.html', image_name = python_data['title'], url = python_data['hdurl'], explanation = python_data['explanation'])

if __name__ == '__main__':
    app.run(debug = True)
