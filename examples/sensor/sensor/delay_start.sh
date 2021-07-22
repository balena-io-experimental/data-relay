#!/bin/sh
#
# Parameters:
#   1 -- Seconds to delay start

echo "Wait $1 seconds before start"
sleep $1
echo "Starting..."

python3 sensor.py
