# dapr Component Plugins

The Data Relay block uses the [PluginBase](http://pluginbase.pocoo.org/) mechanism to identify and configure dapr components. The configuration program finds the expected variable names coded in each plugin and writes a dapr configuration file with the user supplied variable values.

Plugin files must be added in the `plugins` directory. There are two files for each plugin: the `.py` plugin file itself, and a corresponding template `.yaml` file.

## Python file
A plugin is a Python formatted  `.py` file, containing four definitions:

| Variable | Contents                                            |
|----------|-----------------------------------------------------|
| NAME     | Name of plugin (arbitrary)                          |
| TYPE     | Class of plugin; see description below              |
| FILE     | File containing dapr yaml definition template       |
| VARS     | List of variables required by YAML file             |

Example:

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

## YAML file
The YAML file is a template in the form required by dapr to configure a component. An attribute value in the form `!ENV ${<var-name>}` specifies a placeholder for the real value to be replaced by the configuration program.

Example:

```
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: message-queue
spec:
  type: bindings.gcp.pubsub
  version: v1
  metadata:
  - name: topic
    value: !ENV ${GCP_PUBSUB_TOPIC}
  - name: type
    value: !ENV ${GCP_PUBSUB_TYPE}
  - name: project_id
    value: !ENV ${GCP_PUBSUB_PROJECT_ID}
```