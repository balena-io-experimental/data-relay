Uses the Data Relay block to push data from the [balenablocks/sensor](https://github.com/balenablocks/sensor) block to a cloud provider's message queue.

# Configuration
Set the environment variables below as needed.

| Variable | Required? | Notes |
| -------- | :-------: |------ |
| RELAY_OUT_TOPIC | **Y** | Must set to _sensors_ |
|  | **Y** | See cloud block [documentation](https://stupefied-johnson-ee1062.netlify.app/docs/message-queues) for AWS, Azure, etc. service variables |
| | N | See sensor block [documentation](https://github.com/balenablocks/sensor#readme) for variables to set publishing interval, data format and more |
| DAPR_DEBUG | N | Set to _1_ for debug messages in the data_relay log |


# Output
Below is example log output for a BME280 sensor to Azure Event Hubs.

```
13.06.21 09:56:22 (-0400)  data_relay  Data received from local: [{"measurement": "bme280", "fields": {"humidityrelative": 59908.0, "pressure": 101.232257812, "temp": 21140.0}}, {"measurement": "short_UUID", "fields": {"short_uuid": "34793e7"}}]
13.06.21 09:56:22 (-0400)  data_relay  Forwarded data to remote azure-event-hub
```

# Contents

| File/Directory | Notes |
| -------------- | ----- |
| `docker-compose.yml` | standard container configuration file |
| `data_relay`| extra configuration required only if using Azure Key Vault secret store |
| `sensor` | Override `balenablocks/sensor` to delay sensor start to allow the device time to stabilize. |
