Uses the Data Relay block to read input from a message queue in the cloud and simply print data to device log.

# Configuration
Set the environment variables below as needed.

| Variable | Required? | Notes |
| -------- | :-------: | ----- |
| RELAY_IN_TOPIC | **Y** | Must set to `reader-input` |
|  | **Y** | See cloud block [documentation](https://stupefied-johnson-ee1062.netlify.app/docs/message-queues) for AWS, Azure, etc. service variables |
| DAPR_DEBUG | N | Set to _1_ for debug messages in the data_relay log |


# Output
Below is example log output from AWS Simple Queue Service. Must set DAPR_DEBUG variable to receive this output. The 204 response indicates success.

```
25.06.21 19:21:23 (-0400)  data_relay  Data received from remote: bc8b1b0, 06/25/2021 23:12:25, 32.00
25.06.21 19:21:23 (-0400)  data_relay  DEBU[0003] mqtt publishing topic relay-in with data: [34 98 99 56 98 49 98 48 44 32 48 54 47 50 53 47 50 48 50 49 32 50 51 58 49 50 58 50 53 44 32 51 50 46 48 48 34]  app_id=cloudBlock instance=bc8b1b0 scope=dapr.contrib type=log ver=1.2.2
25.06.21 19:21:23 (-0400)  data_sink  reader-input b'bc8b1b0, 06/25/2021 23:12:25, 32.00'
25.06.21 19:21:23 (-0400)  data_relay  Forwarded data to local with response <Response [204]>
```

# Contents

| File/Directory | Notes |
| -------------- | ----- |
| `docker-compose.yml` | standard container configuration file |
| `reader` | app to read and print data from message queue input |
| `data_relay`| extra configuration required only if using Azure Key Vault secret store |


