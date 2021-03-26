#!/bin/bash

if [ "x$DAPR_DEBUG" != "x" ]
then
    DAPR_LOGLEVEL="--log-level debug"
fi

# Load information from secrets plugins
if python3 ./src/autoconfigure.py secrets
then
    sleep 3
    daprd $DAPR_LOGLEVEL --components-path /app/components/secrets --app-id $1 &
    DAPR_PID=$!
    sleep 3
    `python3 ./src/getSecrets.py` # environment variables are applied from stdout
    kill -SIGTERM "$DAPR_PID"
    sleep 5
fi

# Initialize output plugins
python3 ./src/autoconfigure.py output
sleep 3
daprd $DAPR_LOGLEVEL --components-path /app/components --app-protocol grpc --app-port 50051 --app-id $1 &
sleep 3

# Rock'n'roll
python3 ./src/main.py
