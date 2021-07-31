Uses the Data Relay block to push CPU temperature data to an InfluxDB time series database in the cloud. Outputs temperature reading every 30 seconds.

# Configuration
Set the environment variables below as needed.

| Variable | Required? | Notes |
| -------- | :-------: | ----- |
| RELAY_OUT_TOPIC | **Y** | Must set to `cpu_temp` |
| *InfluxDB variables* | **Y** | See [plugin documentation](https://stupefied-johnson-ee1062.netlify.app/docs/influx-db) for specifics |
| DAPR_DEBUG | N | Set to `1` for debug messages in the data_relay log |


# Input and Output
Data from the temperature data source is a JSON object in the form described on the [InfluxDB plugin](https://stupefied-johnson-ee1062.netlify.app/docs/influx-db) documentation page.

```
29.06.21 10:32:54 (-0400)  data_relay  Data received from local: { "measurement": "cpu_temp", "tags":"device=bc8b1b0", "values": "temp=32.0" }
29.06.21 10:32:54 (-0400)  data_relay  Forwarded data to remote influxdb
```

# Contents

| File/Directory | Notes |
| -------------- | ----- |
| `docker-compose.yml` | standard container configuration file |
| `cputemp` | app to generate CPU temperature data |



