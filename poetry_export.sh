#!/bin/bash

# Check if poetry-plugin-export is installed
if ! poetry self show plugins | grep -q poetry-plugin-export; then
    echo "Installing poetry-plugin-export..."
    poetry self add poetry-plugin-export
fi

# Export requirements.txt
DESTINATION=app/requirements.txt
poetry export -f requirements.txt --output $DESTINATION=app/requirements.txt
 --without-hashes --with production
echo "Requirements exported to $DESTINATION=app/requirements.txt."
