#!/bin/bash

if [ "$SECRETS" = "KEYVAULT" ];then
    python3 ./src/autoconfigureSecrets.py 
    sleep 3
    daprd --components-path /app/components --app-id $1 &
    sleep 3
    python3 ./src/getSecrets.py #generates environ variables with the secrets
fi

python3 ./src/autoconfigure.py
sleep 3
daprd --log-level debug --components-path /app/components --app-protocol grpc --app-port 50051 --app-id $1 &
sleep 3
python3 ./src/main.py 
