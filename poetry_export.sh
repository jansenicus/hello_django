#!/bin/bash

# Check if poetry-plugin-export is installed
if ! poetry self show plugins | grep -q poetry-plugin-export; then
    echo "Installing poetry-plugin-export..."
    poetry self add poetry-plugin-export
fi

# Export requirements.txt
DESTINATION=app/requirements.txt
DESTINATION2=app/requirements.txt.dev
poetry lock
echo "Exporting requirements to $DESTINATION and $DESTINATION2..."
# Export production and development requirements
poetry export -f requirements.txt --output $DESTINATION --without-hashes --with production
poetry export -f requirements.txt --output $DESTINATION2 --without-hashes --with dev
echo "Requirements exported to $DESTINATION."
