import time
import requests
import os
import json

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App, BindingRequest

import json

app = App()
dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
# messageQueue_url = "http://localhost:{}/v1.0/bindings/message-queue".format(dapr_port)
blob_url = "http://localhost:{}/v1.0/bindings/blob".format(dapr_port)
bindings = [blob_url]

def sendRequest(data):
    try:
        for url in bindings:
            payload = { "data": data, "operation": "create" }
            response = requests.post(url, json=payload)
            print(response, flush=True)

    except Exception as e:
        print(e, flush=True)

@app.binding('mqtt-input')
def binding(request: BindingRequest):
    print("Data recieved from MQTT: " + request.text(), flush=True)
    sendRequest(request.text())

app.run(50051)