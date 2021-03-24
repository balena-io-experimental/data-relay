import requests
import os
import json

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App, BindingRequest

import json

app = App()
outputComponents = []
daprPort = os.getenv("DAPR_HTTP_PORT", 3500)
baseUrl = "http://localhost:{}/v1.0/bindings/".format(daprPort)

def findComponents():
    try:
        response = requests.get("http://localhost:{}/v1.0/metadata".format(daprPort))
        # print("components found " + str(response.content), flush=True)
        responseJson = json.loads(response.content)
        for component in responseJson["components"]:
            if component["name"] != "mqtt-input":
                outputComponents.append(component["name"])

    except Exception as e:
        print(e, flush=True)

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
    print("Data recieved from MQTT: " + request.text(), flush=True)
    sendRequest(request.text())

findComponents()
app.run(50051)