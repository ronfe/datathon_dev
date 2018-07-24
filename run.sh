#!/usr/bin/env bash

python3.5 process.py
cd frontend
npm i
cd ..
FLASK_APP=server.py flask run
