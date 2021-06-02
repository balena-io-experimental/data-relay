import requests
import os
import json

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App, BindingRequest

import json

app = App()
outputComponents = []
non_output_components = ['aws-secrets-manager', 'gcp-secret-manager', 'azure-keyvault', 'mqtt-input']
daprPort = os.getenv("DAPR_HTTP_PORT", 3500)
baseUrl = "http://localhost:{}/v1.0/bindings/".format(daprPort)

def findComponents():
    """Build list of output components by excluding fixed list of non-output components."""
    try:
        response = requests.get("http://localhost:{}/v1.0/metadata".format(daprPort))
        # print("components found " + str(response.content), flush=True)
        responseJson = json.loads(response.content)
        for component in responseJson["components"]:
            try:
                non_output_components.index(component["name"])
            except ValueError:
                outputComponents.append(component["name"])

    except Exception as e:
        print(e, flush=True)

def sendRequest(data):
    """Sends data to all output components."""
    try:
        for component in outputComponents:
            payload = { "data": data, "operation": "create" }
            response = requests.post(baseUrl + component, json=payload)
            print("Sending to output {output} with response {response}".format(output=component,response=response))

    except Exception as e:
        print(e, flush=True)

@app.binding('mqtt-input')
def binding(request: BindingRequest):
    print("Data received from MQTT: " + request.text(), flush=True)
    sendRequest(request.text())

print("balenablocks/cloud ==> run dapr and relay input to cloud")
findComponents()
app.run(50051)
