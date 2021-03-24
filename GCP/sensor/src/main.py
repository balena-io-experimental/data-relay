import time
import requests
import os

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
messageQueue_url = "http://localhost:{}/v1.0/bindings/messagequeue".format(dapr_port)
#blob_url = "http://localhost:{}/v1.0/bindings/blob".format(dapr_port)
bindings = [messageQueue_url]

n = 0
while True:
    n += 1
    payload = { "data": {"orderId": n}, "operation": "create" }
    print(payload, flush=True)
    try:
        for url in bindings:
            response = requests.post(url, json=payload)
            print(response, flush=True)

    except Exception as e:
        print(e, flush=True)

    time.sleep(10)
