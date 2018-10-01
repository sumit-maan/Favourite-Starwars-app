#!/bin/bash
echo "activating environment..."
source env/bin/activate
echo "installing requirements..."
pip install -r requirements.txt
echo "environment activated..."
cd starwar
echo "run migrations..."
python3 manage.py migrate
echo "starting server..."
python3 manage.py runserver 0.0.0.0:8000

