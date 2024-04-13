#!/bin/bash

# Download gsender.py from GitHub
wget https://raw.githubusercontent.com/realgojo/tg-sender/main/gsender.py

# Install Python3 and pip
sudo apt-get update
sudo apt-get install -y python3 python3-pip

# Install required Python packages
sudo pip3 install -U python-telegram-bot

# Set executable permission for gsender.py
chmod +x gsender.py

# Move gsender.py to /usr/local/bin and rename it to gsender
sudo mv gsender.py /usr/local/bin/gsender

# Create a wrapper script for gsender.py
echo -e '#!/usr/bin/env python3\n' > gsender
echo -e 'from gsender import main\n' >> gsender
echo -e 'if __name__ == "__main__":\n' >> gsender
echo -e '    import asyncio\n' >> gsender
echo -e '    asyncio.run(main())' >> gsender

# Set executable permission for the wrapper script
sudo chmod +x gsender

echo "Installation complete. You can now use 'gsender' command to run the script."
