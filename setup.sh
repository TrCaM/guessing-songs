#!/bin/bash

mkdir protos_out
protoc protos/*.proto --python_out=pyi_out:protos_out
# Get the absolute path of the current directory
current_dir="$(pwd)"

# Create a string containing the path to the file to be created
venv_file="$current_dir/venv/lib/python3.11/site-packages/protos.pth"

# Write the absolute path of the current directory to the venv file
echo "$current_dir/protos_out" > "$venv_file"