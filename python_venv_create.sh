#!/bin/bash

# creating virtual env using python3
sudo python3 -m venv $pwd venvpy3
source venvpy3/bin/activate


# install all default requirements
sudo pip3 install -r requirements.txt

# with system package
virtualenv --system-site-packages
