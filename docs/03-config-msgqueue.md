# Message Queues
This page lists the environment variables or secret store values you must define to use each provider.

## AWS SQS

| Environment Variable Name | Secret Store Key | Description |
|---------------------------|------------------|-------------|
|AWS_SQS_QUEUE_NAME         |aws-sqs-queue-name  | |
|AWS_SQS_REGION             |aws-sqs-region  | |
|AWS_SQS_ACCESS_KEY         |aws-sqs-access-key | |
|AWS_SQS_SECRET_KEY         |aws-sqs-secret-key | |

## Azure Event Hub

| Environment Variable Name | Secret Store Key | Description |
|---------------------------|------------------|-------------|
|AZURE_EH_CONNECTION_STRING   |azure-eh-connection-string  | |
|AZURE_EH_CONSUMER_GROUP      |azure-eh-consumer-group  | |
|AZURE_EH_STORAGE_ACCOUNT     |azure-eh-storage-account | |
|AZURE_EH_STORAGE_ACCOUNT_KEY |azure-eh-storage-account-key | |
|AZURE_EH_CONTAINER_NAME      |azure-eh-container-hame | |

## Google Cloud Pub/Sub

For the variables below, `GCP_PUBSUB_TOPIC` and `GCP_PUBSUB_SUBSCRIPTION` are specific to the data published. However, the other variables are more generally related to the account being used. For a GCP service account these values are available for download when creating the account.

| Environment Variable Name            | Secret Store Key |Description                                 |
|--------------------------------------|------------------|--------------------------------------------|
|GCP_PUBSUB_TOPIC                      |gcp-pubsub-topic  |Name of topic a client uses to publish data messages to the queue |
|GCP_PUBSUB_SUBSCRIPTION               |gcp-pubsub-subscription  |Optional; name of topic a client uses to subscribe to messages from the queue |
|GCP_PUBSUB_TYPE                       |gcp-pubsub-type   | likely *service_account*                   |
|GCP_PUBSUB_PROJECT_ID                 |gcp-pubsub-id     |                                            |
|GCP_PUBSUB_CLIENT_EMAIL               |gcp-pubsub-client-email |Email address                         |
|GCP_PUBSUB_PRIVATE_KEY                |gcp-pubsub-private-key|Actual key for the account, like '-----BEGIN PRIVATE KEY-----\nMII...Gy1\n-----END PRIVATE KEY-----\n'                  |