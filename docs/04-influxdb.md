# InfluxDB
The InfluxDB plugin sends data to the InfluxDB database. This page lists the environment variables you must define, and also describes the required format for incoming data.

## Environment variables
If you use InfluxDB Cloud, see the [*Write data*](https://docs.influxdata.com/influxdb/cloud/write-data/#what-youll-need) documentation for how to find the value for these variables.

| Environment Variable Name | Secret Store Key | Description |
|---------------------------|------------------|-------------|
|INFLUXDB_URL         |influxdb-url  | URL for the organization |
|INFLUXDB_TOKEN       |influxdb-token  | Authentication token suitable for writing data |
|INFLUXDB_ORG         |influxdb-org | ID for the organization |
|INFLUXDB_BUCKET      |influxdb-bucket | Bucket in the database in which to store the data |

## Data Format
Data from the data source must be a JSON object in the form below.

```
{ "measurement": "<measurement-name>", "tags":"<tkey>=<tvalue>,...", "values": "<fkey>=<fvalue>,..." }
```

For example,
```
{ "measurement": "cpu_temp", "tags":"device=bc8b1b0", "values": "temp=32.0" }
```

A tags attribute is optional. The values attribute includes the actual data values. See InfluxDB [line protocol](https://docs.influxdata.com/influxdb/cloud/reference/syntax/line-protocol) for more details.

| Element          |Required?| Notes          |
|------------------|:--:|----------------|
| measurement-name | Y  | Name of measurement|
| tkey          | N  | Key for tag        |
| tvalue        | N  | Value for tag      |
| fkey        | Y  | Key for data field      |
| fvalue      | Y  | Value for data field    |
