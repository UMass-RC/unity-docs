#!/bin/sh

test -e sheets-to-md/unity-sheets-key.json && ( cd sheets-to-md; python sheets-to-md.py )

# run the CMD from the Dockerfile
exec "$@"
