# Google Cloud Storage Variables

For the variables below, `GCP_BLOB_BUCKET` is specific to the data published. However, the other variables are more generally related to the account being used. For a GCP service account these values are available for download when creating the account.

| Environment Variable Name          | Secret Store Key |Description                                 |
|------------------------------------|------------------|--------------------------------------------|
|GCP_BLOB_BUCKET                     |gcp-blob-bucket   | |
|GCP_BLOB_TYPE                       |gcp-blob-type     | likely *service_account* |
|GCP_BLOB_PROJECT_ID                 |gcp-blob-id       | |
|GCP_BLOB_PRIVATE_KEY_ID             |gcp-blob-private-key-id | |
|GCP_BLOB_CLIENT_EMAIL               |gcp-blob-client-email |Email address |
|GCP_BLOB_CLIENT_ID                  |gcp-blob-client-id |                                            |
|GCP_BLOB_AUTH_URI                   |gcp-blob-auth-uri |                                            |
|GCP_BLOB_TOKEN_URI                  |gcp-blob-token-uri |                                            |
|GCP_BLOB_AUTH_PROVIDER_X509_CERT_URL|gcp-blob-auth-provider-x509-cert-url |                          |
|GCP_BLOB_CLIENT_X509_CERT_URL       |gcp-blob-client-x509-cert-url|                                            |
|GCP_BLOB_PRIVATE_KEY                |gcp-blob-private-key|Actual key for the account, like '-----BEGIN PRIVATE KEY-----\nMII...Gy1\n-----END PRIVATE KEY-----\n'                  |

