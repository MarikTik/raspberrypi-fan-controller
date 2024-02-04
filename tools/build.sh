#!/bin/bash

# Define the path to the requirements file
requirements_path="requirements.txt"

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    # Create a virtual environment named 'venv'
    python3 -m venv venv
fi

echo "Activating virtual environment..."
# Activate the virtual environment
source venv/bin/activate

if [ -f "$requirements_path" ]; then
    echo "Installing requirements from $requirements_path..."
    # Install requirements from requirements.txt located one directory above
    pip install -r "$requirements_path"
    echo "Setup complete!"
else
    echo "Requirements file not found at $requirements_path"
fi
