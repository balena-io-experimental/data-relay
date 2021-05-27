# Google Cloud Pub/Sub Variables

For the variables below, `GCP_PUBSUB_TOPIC` is specific to the data published. However, the other variables are more generally related to the account being used. For a GCP service account these values are available for download when creating the account.

| Environment Variable Name            | Secret Store Key |Description                                 |
|--------------------------------------|------------------|--------------------------------------------|
|GCP_PUBSUB_TOPIC                      |gcp-pubsub-topic  |Name of topic on which to post data messages|
|GCP_PUBSUB_TYPE                       |gcp-pubsub-type   | likely *service_account*                   |
|GCP_PUBSUB_PROJECT_ID                 |gcp-pubsub-id     |                                            |
|GCP_PUBSUB_PRIVATE_KEY_ID             |gcp-pubsub-private-key-id |                                    |
|GCP_PUBSUB_CLIENT_EMAIL               |gcp-pubsub-client-email |Email address                         |
|GCP_PUBSUB_CLIENT_ID                  |gcp-pubsub-client-id |                                         |
|GCP_PUBSUB_AUTH_URI                   |gcp-pubsub-auth-uri  |                                         |
|GCP_PUBSUB_TOKEN_URI                  |gcp-pubsub-token-uri |                                         |
|GCP_PUBSUB_AUTH_PROVIDER_X509_CERT_URL|gcp-pubsub-auth-provider-x509-cert-url |                       |
|GCP_PUBSUB_CLIENT_X509_CERT_URL       |gcp-pubsub-client-x509-cert-url|                               |
|GCP_PUBSUB_PRIVATE_KEY                |gcp-pubsub-private-key|Actual key for the account, like '-----BEGIN PRIVATE KEY-----\nMII...Gy1\n-----END PRIVATE KEY-----\n'                  |

