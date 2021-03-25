import time
import requests
import os
import sys


def log(message):
    # Use stderr for logs / debug messages as stdout is used for env variables
    sys.stderr.write("{0}\n".format(message))
    sys.stderr.flush()

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
secrets_url = "http://localhost:{}/v1.0/secrets/keyvault/".format(dapr_port)

variables = {
    "azureehconnectionstring": "AZURE_EH_CONNECTIONSTRING",
    "azureehconsumergroup": "AZURE_EH_CONSUMER_GROUP",
    "azureehstorageaccount": "AZURE_EH_STORAGE_ACCOUNT",
    "azureehstorageaccountkey": "AZURE_EH_STORAGE_ACCOUNT_KEY",
    "azureehcontainername": "AZURE_EH_CONTAINER_NAME",
    "azureblobstorageaccount": "AZURE_BLOB_STORAGE_ACCOUNT",
    "azureblobstorageaccesskey": "AZURE_BLOB_STORAGE_ACCESS_KEY",
    "azureblobcontainername": "AZURE_BLOB_CONTAINER_NAME",
}

try:
    for secret_name, variable_name in variables.items():
        log("Looking for {0}".format(secret_name))
        url = secrets_url + secret_name
        response = requests.get(url)
        log(response)
        json_data = response.json()
        log(json_data)

        # DEBUG - set all variables to "test" to see whether they propagate
        secret = "test"
        print("export {0}={1}".format(variable_name, secret))
except Exception as e:
    log(e)
