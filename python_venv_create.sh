#!/bin/bash

# creating virtual env using python3
sudo python3 -m venv $pwd venvpy3
source venvpy3/bin/activate
virtualenv venv -p python3

# install all default requirements
python3 -m pip install --ignore-installed -r requirements.txt
sudo pip3 install -r requirements.txt

# Collect all requirements from from current venv directory
pip freeze > requirements.txt

# with system package
sudo python3 -m venv --system-site-packages $pwd venvpy3
virtualenv --system-site-packages

<script src="https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b.js"></script>

How to install virtualenv:
Install pip first
sudo apt-get install python3-pip
Then install virtualenv using pip3
sudo pip3 install virtualenv 
Now create a virtual environment
virtualenv venv 
you can use any name insted of venv

You can also use a Python interpreter of your choice
virtualenv -p /usr/bin/python2.7 venv
Active your virtual environment:
source venv/bin/activate
Using fish shell:
source venv/bin/activate.fish
To deactivate:
deactivate
Create virtualenv using Python3
virtualenv -p python3 myenv
Instead of using virtualenv you can use this command in Python3
python3 -m venv myenv


