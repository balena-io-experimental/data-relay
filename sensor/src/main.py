import time
import requests
import os

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App

import json

app = App()
dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
# messageQueue_url = "http://localhost:{}/v1.0/bindings/message-queue".format(dapr_port)
blob_url = "http://localhost:{}/v1.0/bindings/blob".format(dapr_port)
bindings = [blob_url]

@app.subscribe(pubsub_name='mqtt-input', topic='cloud-input')
def mytopic(event: v1.Event) -> None:
    data = json.loads(event.Data())
    print(f'Subscriber received: id={data["id"]}, message="{data["message"]}", content_type="{event.content_type}"',flush=True)

    try:
        for url in bindings:
            response = requests.post(url, json=data)
            print(response, flush=True)

    except Exception as e:
        print(e, flush=True)

app.run(50051)




