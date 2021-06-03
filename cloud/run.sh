#!/bin/bash

if [ "x$DAPR_DEBUG" != "x" ]
then
    DAPR_LOGLEVEL="--log-level debug"
fi

# Place components on tmpfs based file system so they don't remain on disk.
# The user may already have placed components in the expected directory.
component_dir=/app/components
mv $component_dir /tmp
mkdir $component_dir
mount -t tmpfs -o mode=711 tmpfs $component_dir
mv /tmp/components/* $component_dir
rm -rf /tmp/components

# Initialize dapr services from plugins
python3 ./src/autoconfigure.py
sleep 3
daprd $DAPR_LOGLEVEL --components-path /app/components --app-protocol grpc --app-port 50051 --app-id $1 &
sleep 3

# Rock'n'roll
python3 ./src/main.py
