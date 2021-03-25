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
    "azureblobstorageaccountkey": "AZURE_BLOB_STORAGE_ACCOUNT_KEY",
    "azureblobcontainername": "AZURE_BLOB_CONTAINER_NAME",
}

try:
    for secret_name, variable_name in variables.items():
        log("Looking for {0}".format(secret_name))
        url = secrets_url + secret_name
        response = requests.get(url)
        json_data = response.json()

        if response.status_code != 200:
            if "message" in json_data and "StatusCode=404" in json_data["message"]:
                # Secret not found, we do not care
                continue

            # Any other failure - log the details
            log("Getting secrets failed with status code %d".format(response.status_code))
            log(json_data)
            continue

        log("{0} secret found, populating {1} env variable".format(secret_name, variable_name))
        print("export {0}={1}".format(variable_name, json_data[secret_name]))
except Exception as e:
    log(e)
