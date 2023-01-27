#!/bin/bash
PROJECTS_PATH="$HOME" # edit this path

if [[ -z $1 ]]; then
    echo "[!] Project name cannot be none !!"
    exit;
fi

PROJECT_NAME="$1"
PROJECT_PATH="$PROJECTS_PATH/$PROJECT_NAME"

mkdir "$PROJECT_PATH"
mkdir "$PROJECT_PATH/$PROJECT_NAME"
mkdir "$PROJECT_PATH/$PROJECT_NAME/lib"
touch "$PROJECT_PATH/$PROJECT_NAME/lib/__init__.py"
touch "$PROJECT_PATH/$PROJECT_NAME/__init__.py"
touch "$PROJECT_PATH/$PROJECT_NAME/__main__.py"
touch "$PROJECT_PATH/readme.md"

cd "$PROJECT_PATH"
bash -c "python3.11 -m venv .env"
cd "$HOME/Phanes"
