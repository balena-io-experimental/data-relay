Uses the cloud block to push CPU temperature data to an InfluxDB time series database in the cloud. Outputs temperature reading every 30 seconds.

# Configuration
Set the environment variables below as needed.

| Variable | Required? | Notes |
| -------- | :-------: | ----- |
| LOCAL_MQTT_INPUT_TOPIC | **Y** | Must set to `cpu_temp` |
| DAPR_DEBUG | N | Set to _1_ for debug messages in the cloud log |
|  | **Y** | See cloud block [documentation](https://stupefied-johnson-ee1062.netlify.app/docs/message-queues) for AWS, Azure, etc. service variables |


# Input and Output
Data from the termperature data source is a JSON object in the form described on the InfluxDB plugin [documentation page]([documentation](https://stupefied-johnson-ee1062.netlify.app/docs/influxdb).


Below is example log output to an InfluxDB instance. Must set DAPR_DEBUG variable to receive this output.


```
29.06.21 10:32:54 (-0400)  cloud  Data received from local input: { "measurement": "cpu_temp", "tags":"device=bc8b1b0", "values": "temp=32.0" }
29.06.21 10:32:54 (-0400)  cloud  Sent data to remote influxdb
```

# Contents

| File/Directory | Notes |
| -------------- | ----- |
| `docker-compose.yml` | standard container configuration file |
| `cputemp` | app to generate CPU temperature data |



