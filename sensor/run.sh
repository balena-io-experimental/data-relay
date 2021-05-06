#!/bin/bash

if [ "x$DAPR_DEBUG" != "x" ]
then
    DAPR_LOGLEVEL="--log-level debug"
fi

# Initialize dapr services from plugins
python3 ./src/autoconfigure.py
sleep 3
daprd $DAPR_LOGLEVEL --components-path /app/components --app-protocol grpc --app-port 50051 --app-id $1 &
sleep 3

# Rock'n'roll
python3 ./src/main.py
