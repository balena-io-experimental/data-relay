import time
import requests
import os

dapr_pub_port = os.getenv("DAPR_HTTP_PORT", 3500)
dapr_pub_url = "http://localhost:{}/v1.0/bindings/sample-topic".format(dapr_pub_port)

dapr_s3_url = "http://localhost:{}/v1.0/bindings/blob".format(dapr_pub_port)

# Send data to AWS S3
try:
    response = requests.post(dapr_s3_url, json={ "data": {"my_blob_data": 100}, "operation": "create" })
    print(response, flush=True)
except Exception as e:
    print(e, flush=True)

# Send data to AWS SQS
n = 0
while True:
    n += 1
    payload = { "data": {"orderId": n}, "operation": "create" }
    print(payload, flush=True)
    try:
        response = requests.post(dapr_pub_url, json=payload)
        print(response, flush=True)
    except Exception as e:
        print(e, flush=True)

    time.sleep(30)
