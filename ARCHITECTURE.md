# Architecture

The diagram below shows the components of a solution based on the cloud block. The diagram includes some components on the development roadmap that have not yet been implemented.

![Architecture](https://raw.githubusercontent.com/balena-io-playground/data-relay/main/docs/images/architecture.png)

|  Component   | Description                                                                                  |
|--------------|----------------------------------------------------------------------------------------------|
| Data Source  | Your application container, which generates data formatted into MQTT messages                |
| Data Sink    | Your application container, which receives data formatted into MQTT messages                 |
| MQTT         | Message broker to transfer messages to the cloud block                                       |
| Cloud Block  | Container to package and route new data messages to or from a cloud service, based on configuration you provide.|
| cloud service| A supported service at a cloud provider to receive or provide data.                         |

Generally an application includes a data source *or* a data sink but not both. However, it is possible to include both source and sink for the same cloud topic to provide an "echo" application. Any data sent by the data source will be received by the data sink.

## Cloud Block Interfaces
The cloud block makes a distinction between local and remote interfaces. A local interface provides device facing, internal access to the cloud block. In the future it may provide a command interface. A remote interface provides access to external cloud resources. Conceivably an external resource might be located on the device.

Data flows from a local interface, through the cloud block, to a remote interface -- and vice versa. Data does not flow between local interfaces within the cloud block.
