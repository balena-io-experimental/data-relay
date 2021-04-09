import time
import requests
import os
import sys
from util import get_plugin_source


def log(message):
    # Use stderr for logs / debug messages as stdout is used for env variables
    sys.stderr.write("{0}\n".format(message))
    sys.stderr.flush()

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
secrets_url = "http://localhost:{}/v1.0/secrets/keyvault/".format(dapr_port)

variables = {}
plugin_source = get_plugin_source()
for plugin_name in plugin_source.list_plugins():
    plugin = plugin_source.load_plugin(plugin_name)

    if plugin.TYPE == "secrets":
        continue

    for var in plugin.VARS:
        variables[var.replace("_", "-").lower()] = var

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
            log("Getting secrets failed with status code {code}".format(code=response.status_code))
            log("Response: {response}".format(response=json_data))
            continue

        log("{0} secret found, populating {1} env variable".format(secret_name, variable_name))
        print("export {0}={1}".format(variable_name, json_data[secret_name]))
except Exception as e:
    log(e)
