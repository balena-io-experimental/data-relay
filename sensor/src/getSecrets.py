import time
import requests
import os


dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
secrets_url = "http://localhost:{}/v1.0/secrets/keyvault/".format(dapr_port)

variableList = ["AZURE_EH_CONNECTIONSTRING", "AZURE_EH_CONSUMER_GROUP", "AZURE_EH_STORAGE_ACCOUNT", "AZURE_EH_STORAGE_ACCOUNT_KEY", "AZURE_EH_CONTAINER_NAME"]

try:
    for variable in variableList:
        url = secrets_url.variable

        response = requests.get(url)
        json_data = response.json()

        result = json_data._value

        os.putenv(variable, result)
        
    except Exception as e:
        print(e, flush=True)


time.sleep(1)