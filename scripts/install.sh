#!/bin/bash
if [ "$1" == "--dev" ]
then
    pip install --editable .
else
    pip install .
fi