# Many thanks to: https://wikitech.wikimedia.org/wiki/Help:Toolforge/My_first_Flask_OAuth_tool

import os
import yaml

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
from sqlitedict import SqliteDict
import pickle
import math
import re
import json

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

__dir__ = os.path.dirname(__file__)
app.config.update(
    yaml.safe_load(open(os.path.join(__dir__, 'default_config.yaml'))))
try:
    app.config.update(
        yaml.safe_load(open(os.path.join(__dir__, 'config.yaml'))))
except IOError:
    # It is ok if there is no local config file
    pass
print("Try: http://127.0.0.1:5000/api/v1/clickstream?title=Frida_Kahlo")
# Enable CORS for API endpoints
#CORS(app, resources={'*': {'origins': '*'}})
CORS(app)

# db_sources = SqliteDict('sources.sqlite',flag="r")
# db_targets = SqliteDict('targets.sqlite',flag="r")

db_sources = pickle.load(open("sources.pkl", "rb"))
db_targets = pickle.load(open("targets.pkl", "rb"))

@app.route('/api/v1/clickstream', methods=['GET'])
def get_clicks():
    args = parse_args(request)
    title = args['title'] ## pass qid-seed

    sources = db_sources.get(title,{})[:10]
    targets = db_targets.get(title,{})[:10]

    results = {
        "title": title,
        "sources": [{"page":h[0],"type":h[1],"count":h[2]} for h in sources],
        "targets": [{"page":h[0],"type":h[1],"count":h[2]} for h in targets],
    }
    return jsonify(results)

def parse_args(request):
    """
    Parse api query parameters
    """
    title = request.args.get('title').replace(" ","_")

    ## pass arguments
    args = {
        'title': title,
    }

    return args