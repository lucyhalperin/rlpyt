#!/bin/bash

# creating venv and installing requirements
virtualenv venv
source venv/bin/activate
pip3 install atari-py
pip3 install torchvision
pip3 install opencv-python
pip3 install psutil
pip3 install pyprind

python -m atari_py.import_roms ./ROM

#run
python3 example_1.py
