from flask import Flask

from urllib import request
import json

with request.urlopen('http://python.org/') as response:
    html = response.read()
