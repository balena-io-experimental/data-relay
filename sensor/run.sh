#!/bin/bash

if [ "x$DAPR_DEBUG" != "x" ]
then
    DAPR_LOGLEVEL="--log-level debug"
fi

# Ensure directory set up for component configuration files. By default use
# tmpfs to avoid writing secrets to disk/flash. However, allow containing
# Dockerfile/docker-compose to override setup here, for example for development.
component_dir=/app/components
if [ -e  "$component_dir" ]
then
    echo "$component_dir directory already exists"
else
    mkdir "$component_dir"
    mount -t tmpfs -o mode=711 tmpfs "$component_dir"
fi

# Initialize dapr services from plugins
python3 ./src/autoconfigure.py
sleep 3
daprd $DAPR_LOGLEVEL --components-path /app/components --app-protocol grpc --app-port 50051 --app-id $1 &
sleep 3

# Rock'n'roll
python3 ./src/main.py
