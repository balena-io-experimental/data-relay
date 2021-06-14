Example use of the cloud block with the [balenablocks/sensor](https://github.com/balenablocks/sensor) block as input. No user code required!

# Configuration
Set the environment variables below as needed.

| Variable | Required? | Notes |
| -------- | :-------: |------ |
| MQTT_INPUT_TOPIC | **Y** | Must set to _sensors_ |
| DAPR_DEBUG | N | Set to _1_ for debug messages in the cloud log |
|  | **Y** | See cloud block [documentation](https://www.balena.io/docs/learn/develop/integrations/cloud-block-services/aws/) for AWS, Azure, etc. service variables |
| | N | See sensor block [documentation](https://github.com/balenablocks/sensor#readme) for variables to set publishing interval, data format and more |


# Output
Below is example log output for a BME280 sensor to Azure Event Hubs. Must set DAPR_DEBUG variable to receive this output. The 204 response indicates success.

```
13.06.21 09:56:22 (-0400)  cloud  Data received from MQTT: [{"measurement": "bme280", "fields": {"humidityrelative": 59908.0, "pressure": 101.232257812, "temp": 21140.0}}, {"measurement": "short_UUID", "fields": {"short_uuid": "34793e7"}}]
13.06.21 09:56:22 (-0400)  cloud  Sending to output azure-event-hub with response <Response [204]>
```

# Contents

| File/Directory | Notes |
| -------------- | ----- |
| `docker-compose.yml` | standard container configuration file |
| `cloud`| extra configuration required only if using Azure Key Vault secret store |
