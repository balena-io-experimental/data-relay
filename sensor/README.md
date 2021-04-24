# Implementation README

This README is specific to development of the Python implementation.

## dapr Component Plugins

Uses [PluginBase](http://pluginbase.pocoo.org/) plugin mechanism . Plugin files must be added in the `plugins` directory.

A plugin is a Python formatted  `.py` file, containing four definitions:

| Variable | Contents                                            |
|----------|-----------------------------------------------------|
| NAME     | Name of plugin (arbitrary)                          |
| TYPE     | Class of plugin; see description below              |
| FILE     | File containing dapr yaml definition template       |
| VARS     | List of environment variables required by yaml file |

See the example below:

```
NAME = "GCP Pubsub"
TYPE = "output"
FILE = "GcpPubsubOutput.yaml"
VARS = [
    "GCP_PUBSUB_TOPIC",
    "GCP_PUBSUB_TYPE",
    "GCP_PUBSUB_PROJECT_ID",
]
```

A plugin TYPE must be one of the items in the table below.

| Type   | Description                                  |
|--------|----------------------------------------------|
| output |dapr definition to write output data to cloud |
| input  |dapr definition to read input data from device|
| secret |dapr definition to read a secret store        |
