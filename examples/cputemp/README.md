Uses the cloud block to push CPU temperature data to a cloud message queue. Outputs temperature reading every 30 seconds.

# Configuration
Set the environment variables below as needed.

| Variable | Required? | Notes |
| -------- | :-------: | ----- |
| LOCAL_MQTT_INPUT_TOPIC | **Y** | Must set to _cpu_temp_ |
| DAPR_DEBUG | N | Set to _1_ for debug messages in the cloud log |
|  | **Y** | See cloud block [documentation](https://stupefied-johnson-ee1062.netlify.app/docs/message-queues) for AWS, Azure, etc. service variables |


# Output
Below is example log output to GCP Pub/Sub. Must set DAPR_DEBUG variable to receive this output.

```
13.06.21 11:25:04 (-0400)  cloud  Data received from local input: bc8b1b0, 06/13/2021 15:25:04, 31.00
13.06.21 11:25:04 (-0400)  cloud  Sending to output gcp-pubsub
```

# Contents

| File/Directory | Notes |
| -------------- | ----- |
| `docker-compose.yml` | standard container configuration file |
| `cputemp` | app to generate CPU temperature data |
| `cloud`| extra configuration required only if using Azure Key Vault secret store |


