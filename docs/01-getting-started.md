# Getting Started
This page provides a simple example use of the cloud block to help you get started. The diagram below shows how the cloud block forwards data to a cloud messaging service. On the left is a balena device with three containers, where a data source publishes data to MQTT on some source topic to which the cloud block also subscribes. The cloud block then applies the user supplied configuration to forward the data to the provider's message queue service -- whether it's AWS SQS, Azure Event Hubs, or Google Pub/Sub.

![message-app](https://raw.githubusercontent.com/balena-io-playground/cloudBlock/main/docs/images/message-app.png)

Follow these steps to implement the data flow in the diagram.

 1. Define data source and cloud block services for balena device
 1. Create balena application and environment variables
 1. Push service definitions to balenaCloud
 1. Provision device

To illustrate how the cloud block works, we will use a data source that takes temperature readings from the device's CPU. These readings are readily available and do not require hardware or software setup.

We will send these readings to AWS Simple Queue Service (SQS) as JSON data messages. However, as you can see on the [Message Queues](message-queues) page, you also may send these messages to Azure Event Hubs or Google Pub/Sub by defining the environment variables required by each service.

## Define device services

As shown in the architecture diagram above, our goal is to push data to a source topic on an MQTT broker on the balena device. We then wire the cloud block to subscribe to the source topic. See the [example application](https://github.com/kb2ma/cloudBlock-test/tree/main/cputemp) for the CPU temperature reader that does just that.

As shown in the [docker-compose.yml](https://github.com/kb2ma/cloudBlock-test/blob/main/cputemp/docker-compose.yml) for our example application, you must define three services, also shown in the table below.

| Service    | Notes                                                                                                                                                       |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| data_source|Your service to generate data and publish to an MQTT topic                                                                                                   |
| mqtt       |Generic broker service, like [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto)                                                                   |
| cloud      |                                                                                         balena block service that subscribes to `data_source` service messages|

Later, you will push these service definitions to balena cloud as described below. Of course you may wish to push the services locally during development, as described in the balena Develop Locally instructions.

### Data source topic
For our example application, [data_source/main.py](https://github.com/kb2ma/cloudBlock-test/blob/main/cputemp/cputemp/main.py) takes a temperature reading every 30 seconds, and publishes the reading to the *cpu_temp* MQTT topic. We must adapt the cloud block to subscribe to the *cpu_temp* topic used by the data source. By default the cloud block subscribes to the topic *cloud-block-input*. The default may be overridden by defining an environment variable, as shown in the next section.

## Create application
From your balenaCloud account, create a Microservices or Starter application as described in the balena [Getting Started](https://www.balena.io/docs/learn/getting-started/raspberrypi3/nodejs/) instructions. Next, you must define environment variables for the application that configure the cloud block, as described here. The example here uses the AWS Simple Queue Service. To use the Azure or Google Cloud message queues, see the [Message Queues](message-queues) setup page.

### SQS variables
These variables are specific to use of the AWS SQS service.

| Variable         | Notes                                                                             |
|------------------|-----------------------------------------------------------------------------------|
|AWS_SQS_QUEUE_NAME|Name of the queue. Identified as `<cloud-topic>` in the architecture diagram above.|
|AWS_SQS_REGION    |AWS region in which the queue is defined                                           |
|AWS_SQS_ACCESS_KEY|IAM access key ID                                                                  |
|AWS_SQS_SECRET_KEY|IAM secret key for access key                                                      |

We assume you define the variables as balena Environment Variables. You also may define them in a Secret store as described on the [Configuration](configuration#configuration-via-secret-store) page.

See the [SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) for help setting up the queue service. See the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) for help setting up the identity. The IAM User must at least be assigned the SQS *SendMessage* permission.

### Cloud block variables
These variables configure the cloud block on the balena device. They do not depend on the cloud provider.

| Variable              | Notes                                                                                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|MQTT_INPUT_TOPIC |MQTT topic to which the cloud block subscribes for messages from the data source. Identified as `<source-topic>` in the architecture diagram above. Defaults to *cloud-input*. |
|DAPR_DEBUG       |Define as 1 to write debug messages to the *cloud* service log                                                                                                   |

## Push app to balenaCloud and provision device
Once you have defined the application, you may push the service definitions created above to balenaCloud with the `balena push <app-name>` CLI command. See the balena Getting Started instructions for details.

Finally, provision a device with the application you created! When the application runs with the DAPR_DEBUG variable defined, you should see data being pushed to the cloud, like below:

![cputemp-log](https://raw.githubusercontent.com/balena-io-playground/cloudBlock/main/docs/images/cputemp-log.png)
