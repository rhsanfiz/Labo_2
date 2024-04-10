#!/bin/bash 

#echo hello-world

if [ ! -d "codigos" ]; then
    python3 -m virtualenv codigos
fi

source codigos/bin/activate

pip install scipy
pip install numpy
pip install pandas
pip install matplotlib