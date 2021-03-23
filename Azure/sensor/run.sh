#!/bin/bash

daprd --components-path /app/components --app-id $1 &
sleep 3
python3 ./src/main.py 