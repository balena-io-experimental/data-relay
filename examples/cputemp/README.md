Example use of the cloud block with CPU temperature data as input. Outputs temperature reading every 30 seconds.

# Configuration
Set the environment variables below as needed.

| Variable | Required? | Notes |
| -------- | :-------: | ----- |
| MQTT_INPUT_TOPIC | **Y** | Must set to _cpu_temp_ |
| DAPR_DEBUG | N | Set to _1_ for debug messages in the cloud log |
|  | **Y** | See cloud block [documentation](https://www.balena.io/docs/learn/develop/integrations/cloud-block-services/aws/) for AWS, Azure, etc. service variables |


# Output
Below is example log output to GCP Pub/Sub. Must set DAPR_DEBUG variable to receive this output. The 204 response indicates success.

```
13.06.21 11:25:04 (-0400)  cloud  Data received from MQTT: bc8b1b0, 06/13/2021 15:25:04, 31.00
13.06.21 11:25:04 (-0400)  cloud  Sending to output gcp-pubsub with response <Response [204]>
```

# Contents

| File/Directory | Notes |
| -------------- | ----- |
| `docker-compose.yml` | standard container configuration file |
| `cputemp` | app to generate CPU temperature data |
| `cloud`| extra configuration required only if using Azure Key Vault secret store |


