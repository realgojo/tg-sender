#!/bin/bash

# Download gsender.py from GitHub
wget https://raw.githubusercontent.com/realgojo/tg-sender/main/gsender.py

# Install Python3 and pip
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install required Python packages
sudo pip3 install -U python-telegram-bot

# Create a symbolic link to make the script accessible globally
sudo ln -s $(pwd)/gsender.py /usr/local/bin/gsender

echo "Installation complete. You can now use 'gsender' command to run the script."
