#!/bin/sh
#
# Parameters:
#   1 -- Application ID for dapr
#   2 -- Seconds to delay start

if [ "x$DAPR_DEBUG" != "x" ]
then
    DAPR_LOGLEVEL="--log-level debug"
fi

# Place dapr components on tmpfs based file system so they don't remain on disk.
# Copy in any components the user already has placed in the target directory.
component_dir=/app/components
mv $component_dir /tmp
mkdir $component_dir
mount -t tmpfs -o mode=711 tmpfs $component_dir
mv /tmp/components/* $component_dir
rm -rf /tmp/components

# Allow time for networking and MQTT to stabilize.
echo "Wait $2 seconds before start"
sleep $2
echo "Starting..."

# Initialize dapr services from plugins
python3 ./src/autoconfigure.py
sleep 3
# Run dapr sidecar, where main app below listens to sidecar via a gRPC server
daprd $DAPR_LOGLEVEL --components-path /app/components --app-protocol grpc --app-port 50051 --app-id $1 &
sleep 3

# Run main app, which uses sidecar to relay requests/responses between local
# and remote (cloud) components.
python3 ./src/main.py
