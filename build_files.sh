#!/bin/bash
python3.12 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3.12 src/manage.py collectstatic --noinput