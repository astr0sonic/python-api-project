#!/usr/bin/env bash

python3.11 -m venv --clear .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
deactivate
