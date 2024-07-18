#!/bin/bash
python -c "import build" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Could not find 'build'. Installing it..."
    pip install build
    echo 'Install build successfully.'
fi

python -m build