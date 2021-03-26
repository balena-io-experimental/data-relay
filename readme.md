# balenaBlocks/cloud #
A balenaBlock to provide low-friction push of application data to cloud providers including Microsoft Azure, Amazon AWS and Google Cloud Platform. Also accepts data pushed *from* the cloud provider. The `cloud` block itself is a docker image based on the [dapr.io](https://dapr.io/) utility.


## Architecture

The diagram below shows the components of a solution based on the cloud block. The data source, MQTT, and cloud block run on your balena device.

![Architecture](architecture.png)

|  Component   | Description                                                                                  |
|--------------|----------------------------------------------------------------------------------------------|
| Data Source  | Your application container, which generates data formatted into MQTT messages                |
| MQTT         | Message broker to transfer messages to the cloud block                                       |
| Cloud Block  | Packages and routes new data messages to a cloud service, based on configuration you provide.|
| Cloud Service| A supported service at a cloud provider to receive the data. See the list of supported services in the section below on plugins.                                  |


### Cloud Service Plugins

The cloud block uses a flexible plugin capability to allow you to specify the service you wish to receive application data. Presently the cloud block supports the services below.

| Service           | Type          |
|-------------------|---------------|
| AWS SQS           | message queue |
| Azure Event Hubs  | message queue |
| GCP Pub/Sub       | message queue |
| AWS S3            | object storage|
| Azure Blob Storage| object storage|
| GCP Cloud Storage | object storage|
