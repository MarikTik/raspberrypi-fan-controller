#!/bin/bash

# Define the path to the Python script
PYTHON_SCRIPT="/home/pi/fan-controller/src/main.py"

# Create the wrapper script
echo "#!/bin/bash
nohup python3 $PYTHON_SCRIPT \"\$@\"
" > fan

# Make the wrapper script executable
chmod +x fan

# Move the wrapper script to /usr/local/bin to make it available as a command
sudo mv fan /usr/local/bin/fan

# echo "#!/bin/bash
# # Redirect stdout and stderr to /dev/null to suppress output
# nohup python3 $PYTHON_SCRIPT \"\$@\" >/dev/null 2>&1 &
# # Disown the process so it's not terminated when the terminal closes
# disown
# " > fan
 