#!/usr/bin/env bash

BASE_DIR="$(dirname "$(realpath "$0")")"

source .venv/bin/activate
export PYTHONPATH=${BASE_DIR}
python src/main.py
