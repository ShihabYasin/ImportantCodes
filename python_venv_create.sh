#!/bin/bash

# creating virtual env using python3
sudo python3 -m venv $pwd venvpy3
source venvpy3/bin/activate


# install all default requirements
python3 -m pip install --ignore-installed -r requirements.txt
sudo pip3 install -r requirements.txt

# with system package
sudo python3 -m venv --system-site-packages $pwd venvpy3
virtualenv --system-site-packages




