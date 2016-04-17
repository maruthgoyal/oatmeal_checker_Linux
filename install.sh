#!/bin/bash

echo "Please enter your password to continue. It is required to install the following setup tools: PIP, VIRTUALENV"

# Installing pip and virtualenv system-wide
sudo apt-get install python-setuptools
sudo -H easy_install pip
sudo pip install virtualenv

# Installing lib to send desktop notifications
sudo apt-get install libnotify-bin

#Setting up the virtual environment to avoid installing libraries system wide unnecesarily
virtualenv venv
source venv/bin/activate
pip install beautifulsoup4

# Deactivating virtualenv
deactivate
