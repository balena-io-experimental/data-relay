# Message Queues
A message queue supports both sending data to the queue and receiving new data from the queue. This page lists the environment variables or secret store values you must define to use each provider. Also see [Send vs. Receive Data](configuration#send-vs-receive-data) on the Configuration page.

## AWS SQS
`AWS_SQS_QUEUE_NAME` and `AWS_SQS_REGION` are specific to the queue. Other variables are more generally related to the account being used. The IAM User must at least have SQS *SendMessage* and/or *ReadMessage* permissions depending on use.

| Application Variable Name | Secret Store Key | Description |
|---------------------------|------------------|-------------|
|AWS_SQS_QUEUE_NAME         |aws-sqs-queue-name  |Name of SQS queue for publish/subscribe |
|AWS_SQS_REGION             |aws-sqs-region  |Region containing the queue |
|AWS_SQS_ACCESS_KEY         |aws-sqs-access-key | |
|AWS_SQS_SECRET_KEY         |aws-sqs-secret-key |For access key |

## Azure Event Hub
The subscription for the managed identity must include the *Azure Event Hubs Data Sender* and/or *Azure Event Hubs Data Receiver* roles depending on use.

| Application Variable Name | Secret Store Key | Description |
|---------------------------|------------------|-------------|
|AZURE_EH_CONNECTION_STRING   |azure-eh-connection-string  |From shared access policy for Event Hubs instance |
|AZURE_EH_CONSUMER_GROUP      |azure-eh-consumer-group  |For Event Hubs instance |
|AZURE_EH_STORAGE_ACCOUNT     |azure-eh-storage-account | |
|AZURE_EH_STORAGE_ACCOUNT_KEY |azure-eh-storage-account-key | |
|AZURE_EH_CONTAINER_NAME      |azure-eh-container-hame |Name of container for messages in storage account |

## Google Cloud Pub/Sub

`GCP_PUBSUB_TOPIC` and `GCP_PUBSUB_SUBSCRIPTION` are specific to the data published. However, the other variables are more generally related to the account being used. For a GCP service account these values are available for download when creating the account. The account must at least have *Pub/Sub Publisher* and/or *Pub/Sub Subscriber* permissions depending on use.

| Application Variable Name            | Secret Store Key |Description                                 |
|--------------------------------------|------------------|--------------------------------------------|
|GCP_PUBSUB_TOPIC                      |gcp-pubsub-topic  |Name of topic a client uses to publish data messages to the queue |
|GCP_PUBSUB_SUBSCRIPTION               |gcp-pubsub-subscription  |Optional; name of topic a client uses to subscribe to messages from the queue |
|GCP_PUBSUB_TYPE                       |gcp-pubsub-type   | likely *service_account*                   |
|GCP_PUBSUB_PROJECT_ID                 |gcp-pubsub-id     |                                            |
|GCP_PUBSUB_CLIENT_EMAIL               |gcp-pubsub-client-email |Email address                         |
|GCP_PUBSUB_PRIVATE_KEY                |gcp-pubsub-private-key|Actual key for the account, like '-----BEGIN PRIVATE KEY-----\nMII...Gy1\n-----END PRIVATE KEY-----\n'                  |