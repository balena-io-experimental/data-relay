#!/bin/bash

python3 ./src/autoconfigure.py
sleep 3
daprd --log-level debug --components-path /app/components --app-protocol grpc --app-port 50051 --app-id $1 &
sleep 3
python3 ./src/main.py 