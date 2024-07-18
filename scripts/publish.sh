#!/bin/bash
if [ "$1" == "--dev" ]; then
    twine upload --repository testpypi  dist/*
elif [ "$1" == "--prod" ]; then
    twine upload dist/*
else
    echo 'Usage: publish.sh [--dev] [--prod]'
    exit 1
fi