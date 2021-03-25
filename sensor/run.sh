#!/bin/bash

if [ "$SECRETS" = "KEYVAULT" ];then
    python3 ./src/autoconfigureSecrets.py 
    sleep 3
    daprd --components-path /app/components --app-id $1 &
    DAPR_PID=$!
    sleep 3
    python3 ./src/getSecrets.py #generates environ variables with the secrets
    kill -SIGTERM "$DAPR_PID"
    sleep 3
fi

python3 ./src/autoconfigure.py
sleep 3
daprd --log-level debug --components-path /app/components --app-protocol grpc --app-port 50051 --app-id $1 &
sleep 3
python3 ./src/main.py 
