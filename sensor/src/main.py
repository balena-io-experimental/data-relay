import requests
import os
import json

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App, BindingRequest

import json

app = App()
outputComponents = []
non_output_components = []
daprPort = os.getenv("DAPR_HTTP_PORT", 3500)
baseUrl = "http://localhost:{}/v1.0/bindings/".format(daprPort)

def findComponents():
    try:
        response = requests.get("http://localhost:{}/v1.0/metadata".format(daprPort))
        # print("components found " + str(response.content), flush=True)
        responseJson = json.loads(response.content)
        for component in responseJson["components"]:
            # Ensure component is *not* in list of non-output components
            try:
                non_output_components.index(component["name"])
            except ValueError:
                outputComponents.append(component["name"])

    except Exception as e:
        print(e, flush=True)

def build_non_output_list():
    """Builds the list of non-output components from the 'non-output-components' file"""
    global non_output_components
    with open('non-output-components.txt', 'r') as f:
        for line in (x.strip() for x in f):
            non_output_components.append(line)

def sendRequest(data):
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
build_non_output_list()
findComponents()
app.run(50051)
