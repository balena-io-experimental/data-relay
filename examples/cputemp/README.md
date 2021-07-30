Uses the Data Relay block to push CPU temperature data to a cloud provider's message queue. Outputs temperature reading every 30 seconds.

# Configuration
Set the environment variables below as needed.

| Variable | Required? | Notes |
| -------- | :-------: | ----- |
| RELAY_OUT_TOPIC | **Y** | Must set to `cpu_temp` |
|  | **Y** | See Data Relay block [documentation](https://stupefied-johnson-ee1062.netlify.app/docs/message-queues) for AWS, Azure, etc. service variables |
| DAPR_DEBUG | N | Set to _1_ for debug messages in the data_relay log |


# Output
Below is example log output to GCP Pub/Sub.

```
13.06.21 11:25:04 (-0400)  data_relay  Data received from local: bc8b1b0, 06/13/2021 15:25:04, 31.00
13.06.21 11:25:04 (-0400)  data_relay  Forwarded data to remote gcp-pubsub
```

# Contents

| File/Directory | Notes |
| -------------- | ----- |
| `docker-compose.yml` | standard container configuration file |
| `cputemp` | app to generate CPU temperature data |
| `data_relay`| extra configuration required only if using Azure Key Vault secret store |


