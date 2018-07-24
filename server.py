from flask import Flask, json, request, jsonify, redirect, url_for
from flask_cors import CORS
from pymongo import MongoClient
from name_ge import NameGenerator
from verify_file import verify_file
import os
import uuid
import config
import datetime

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
cfg = config.Config()

UPLOAD_PATH = cfg.local_path + '/scripts'
ALLOWED_EXTENSIONS = {'py'}
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

with MongoClient(cfg.db_path) as conn:
    db = conn[cfg.db_name]

ng = NameGenerator()


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/users')
def get_users():
    users = db['users']
    l = list(users.find({}))
    candidates = list()
    na_candidates = list()
    for doc in l:
        if doc["joinedTeam"] is None:
            candidates.append(doc['name'])
        else:
            na_candidates.append(doc['name'])

    return jsonify({"candidates": candidates, "naCandidates": na_candidates})


@app.route('/teamName')
def get_team_name():
    x = ng.generate()
    return jsonify({"name": x})


@app.route('/teamLogs/<path:teamName>')
def get_log_by_team(teamName):
    docs = db['logs'].find({"teamName": teamName})
    result = list()
    for doc in docs:
        t = dict()
        t['status'] = doc['status']
        t['uploadTime'] = doc['uploadTime'].strftime('%Y%m%d - %h%m%s')
        t['uid'] = doc['uid']
        result.append(t)

    return jsonify({"data": result})

@app.route("/joinTeam", methods=['POST'])
def regist_team():
    team_info = json.loads(request.data)
    uid = uuid.uuid1()
    r = {
        "name": team_info["teamName"],
        "users": team_info["users"],
        "submissions": [],
        "highestScore": [0, 0, 0, 0],
        "matchInfo": [],
        "rank": {
            "low": None,
            "med": None,
            "high": None,
            "rand": None
        },
        "uid": uid
    }
    db['teams'].insert_one(r)
    for u in team_info["users"]:
        db["users"].find_one_and_update({"name": u}, {"$set": {"joinedTeam": r["name"]}})

    return jsonify({"status": "OK", "uid": uid})


## upload scripts api
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"status": "failed"})

        file = request.files['file']
        if file.filename == '':
            return jsonify({"status": "failed"})
        if file and allowed_file(file.filename):
            doc = dict()
            file_id = str(uuid.uuid1())
            doc["uuid"] = file_id
            doc["teamName"] = request.form['teamName']
            doc['uploadTime'] = datetime.datetime.now()
            doc['status'] = 'VerificationFailed'

            filename = file_id + '.py'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            x = verify_file(file_id)
            if x['status'] == 'OK':
                doc['status'] = 'Active'

                # update prev active to inactive
                db['logs'].update_one({"teamName": doc["teamName"], "status": "Active"}, {"$set": {"status": "Legacy"}})

            # insert this record
            db['logs'].insert_one(doc)
            return jsonify(x)
