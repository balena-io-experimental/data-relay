# Google Cloud Pub/Sub Environment Variables

For the variables below, `GCP_PUBSUB_TOPIC` is specific to the data published. However, the other variables are more generally related to the account being used. For a GCP service account these values are available for download when creating the account.

| Name                                 | Example                                                                                         |Description                                 |
|--------------------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------|
|GCP_PUBSUB_TOPIC                      |my_data                                                                                          |Name of topic on which to post data messages|
|GCP_PUBSUB_TYPE                       |service_account                                                                                  |                                            |
|GCP_PUBSUB_PROJECT_ID                 |cloud-block-1                                                                                    |                                            |
|GCP_PUBSUB_PRIVATE_KEY_ID             |b56...09b                                                                                        |                                            |
|GCP_PUBSUB_CLIENT_EMAIL               |service@cloud-block-1.iam.gserviceaccount.com                                                    |                                            |
|GCP_PUBSUB_CLIENT_ID                  |111...922                                                                                        |                                            |
|GCP_PUBSUB_AUTH_URI                   |https://accounts.google.com/o/oauth2/auth                                                        |                                            |
|GCP_PUBSUB_TOKEN_URI                  |https://oauth2.googleapis.com/token                                                              |                                            |
|GCP_PUBSUB_AUTH_PROVIDER_X509_CERT_URL|https://www.googleapis.com/oauth2/v1/certs                                                       |                                            |
|GCP_PUBSUB_CLIENT_X509_CERT_URL       |https://www.googleapis.com/robot/v1/metadata/x509/service%40cloud-block-1.iam.gserviceaccount.com|                                            |
|GCP_PUBSUB_PRIVATE_KEY                |-----BEGIN PRIVATE KEY-----\nMII...Gy1\n-----END PRIVATE KEY-----\n                              |Actual key for the account                  |

