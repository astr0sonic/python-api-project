#!/usr/bin/env bash

BASE_DIR="$(dirname "$(realpath "$0")")"
cd "${BASE_DIR}"

python3.11 -m venv --clear .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
deactivate
