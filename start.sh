#!/usr/bin/env bash

BASE_DIR="$(dirname "$(realpath "$0")")"
cd "${BASE_DIR}"

source .venv/bin/activate
export PYTHONPATH="$PWD"
python src/main.py
