# Architecture and Roadmap

The diagram below shows the Data Relay block and related components.

![Architecture](https://raw.githubusercontent.com/balena-io-playground/data-relay/main/docs/images/architecture.png)

|  Component   | Description                                                                                  |
|--------------|----------------------------------------------------------------------------------------------|
| Data Producer  | Your application container, which generates data formatted into MQTT messages                |
| Data Consumer    | Your application container, which receives data formatted into MQTT messages                 |
| MQTT         | Message broker to transfer messages to the Data Relay block                                       |
| Data Relay block  | Container to package and route new data messages to or from a cloud service, based on configuration you provide.|
| cloud service| A supported service at a cloud provider to receive or provide data.                         |

Generally an application includes a data producer or a data consumer but not both.

The Data Relay block distinguishes between internal and external interfaces. An internal interface provides local access to the Data Relay block. An external interface provides access to remote resources on another host or in the cloud.

Data flows from an internal interface, through the Data Relay block, to an external interface -- and vice versa. Data does not flow between internal interfaces within the Data Relay block.


## RESTful resource access
Presently Data Relay block assumes that any data intended for output is sent to all defined external cloud services. So if both a message queue and InfluxDB are defined, outbound data is sent to both. To direct some data to a single output, we plan to provide a separate topic for each in the device's MQTT network.

![Architecture-RESTful](https://raw.githubusercontent.com/balena-io-playground/data-relay/main/docs/images/architecture-restful.png)

For example, to send a message explicitly to InfluxDB, use the `influxdb` MQTT topic. Eventually, we can distinguish between resources within a capability, for example `azure-event-hub/sensor` and `azure-event-hub/monitor`.

## Data transformation
An application data producer on a device and its consumer in the cloud may not agree on the format for the data. In this case it is useful to be able to transform data between formats. For example, the balena [sensor block](https://github.com/balenablocks/sensor#data) format differs from the [InfluxDB adapter](https://stupefied-johnson-ee1062.netlify.app/docs/influx-db#data-format).

We can solve this problem with a Transformer container at the MQTT level on the device or within the Data Relay block, as shown in the diagram below. If transformation occurs at the MQTT level, it becomes easier for anyone to contribute a transformation.

![Architecture-Transformer](https://raw.githubusercontent.com/balena-io-playground/data-relay/main/docs/images/architecture-transformer.png)

Tranformations fall into several categories:

  * simple reformatting
  * caching, to accommodate network downtime
  * aggregation
  * chain of transformation (compound/pipeline)

[Kuiper](https://docs.emqx.io/en/kuiper/latest/) is a generic tool for data transformation and filtering, used by EdgeX. It might be worthwhile to adopt.

## Blob storage and other cloud capabilities
Dapr provides many integrations we may wish to support.. The major cloud providers provide supported blob storage, like AWS S3. Other options include Twilio, MySQL, and SMTP. Blob storage also would benefit from the ability to read/write to a file, which may be considered a kind of tranformation.


## Session security
placeholder
