# Getting Started
This page provides a simple example use of the Data Relay block to help you get started. The diagram below shows how the Data Relay block forwards data to a cloud messaging service. On the left is a balena device with three containers, where a data producer publishes data to MQTT on some topic to which the Data Relay block subscribes. The Data Relay block then applies a user supplied configuration to forward the data out to the provider's message queue service -- whether it's AWS SQS, Azure Event Hubs, or Google Pub/Sub.

![message-app](https://raw.githubusercontent.com/kb2ma/data-relay/landr_for_data_relay/docs/images/message-app.png)

Follow these steps to implement the data flow in the diagram.

 1. Define a data producer and Docker Compose script for the services on the device
 1. Create a balena application and configure variables
 1. Push the Compose script to build and run the containers for the app

In this example we use a data source that takes temperature readings from the device's CPU. These readings are readily available and do not require hardware or software setup.

We send these readings to AWS Simple Queue Service (SQS) as JSON data messages. However, as you can see on the [Message Queues](message-queues) page, you also may send these messages to Azure Event Hubs or Google Pub/Sub by defining the environment variables required by each service.

## Define device services

As shown in the diagram above, our first goal is to push data to a producer topic on an MQTT broker on the balena device. We then wire the Data Relay block to subscribe to the producer topic. See the [CPU Temperature](https://github.com/kb2ma/data-relay/tree/landr_for_data_relay/examples/cputemp) application for an example that does just that.

As shown in the [Docker Compose](https://github.com/kb2ma/data-relay/blob/landr_for_data_relay/examples/cputemp/docker-compose.yml) script for our example application, you must define three services, also shown in the table below.

| Service    | Notes                                                                                                                                                       |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data_source|Your service to produce data and publish to an MQTT topic                                                                                                   |
| mqtt       |Generic broker implementation, like [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto)                                                                   |
| data_relay      |                                                                                         balena block service that subscribes to `data_source` messages|

Later you will push these service definitions to balenaCloud as a balena application. Alternatively you may push the services to your device locally during development, as described in the balena [Develop Locally](https://www.balena.io/docs/learn/develop/local-mode/) instructions.

### Data producer topic
For our example application, [data_source/main.py](https://github.com/kb2ma/data-relay/blob/landr_for_data_relay/examples/cputemp/cputemp/main.py) takes a temperature reading every 30 seconds, and publishes the reading to the *cpu_temp* MQTT topic. We will adapt the Data Relay block to subscribe to the *cpu_temp* topic used by the data source in the next section.

## Create balena application
From your balenaCloud account, create a Microservices or Starter application as described in the balena [Getting Started](https://www.balena.io/docs/learn/getting-started/raspberrypi3/nodejs/) instructions. Next, you must define variables for the application that configure the Data Relay block. The example here uses the AWS Simple Queue Service. To use the Azure or Google Cloud message queues, see the [Message Queues](message-queues) setup page.

### SQS variables

| Variable         | Notes                                                                             |
|------------------|-----------------------------------------------------------------------------------|
|AWS_SQS_QUEUE_NAME|Name of the queue. Identified as `cloud-topic` in the architecture diagram above.|
|AWS_SQS_REGION    |AWS region in which the queue is defined                                           |
|AWS_SQS_ACCESS_KEY|IAM access key ID                                                                  |
|AWS_SQS_SECRET_KEY|IAM secret key for access key                                                      |

We assume you define the variables as balena application Variables. You also may define them in a Secret store as described on the [Configuration](configuration#configuration-via-secret-store) page.

See the [SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) for help setting up the queue service. See the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) for help setting up the identity. The IAM User must at least be assigned the SQS *SendMessage* permission.

### Data Relay block variables
These variables configure the Data Relay block on the balena device. They do not depend on the cloud provider.

| Variable              | Required? | Notes                                                                                                                                             |
|----------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
|LOCAL_MQTT_INPUT_TOPIC | **Y** |MQTT topic to which the Data Relay block subscribes for messages from the data source. Identified as *producer-topic* in the architecture diagram above. Defaults to `cloud-input`. Requires `cpu_temp` in the example application. |
|DAPR_DEBUG       | N |Define as `1` to write debug messages to the *data_relay* service log                                                                                                   |

## Push app to balenaCloud
Once you have defined the application, you may push the service definitions created above to balenaCloud with the `balena push <app-name>` CLI command. See the balena [Getting Started](https://www.balena.io/docs/learn/getting-started/raspberrypi3/nodejs/#add-release) instructions for details.

After a device has downloaded the app services, its log should show data being pushed to the cloud, like below.

![cputemp-log](https://raw.githubusercontent.com/kb2ma/data-relay/landr_for_data_relay/docs/images/cputemp-log.png)
