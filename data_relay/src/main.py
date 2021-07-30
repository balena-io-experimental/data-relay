"""
Connects data flows between local interfaces and remote (cloud) interfaces
using the configured dapr components.

Copyright 2021 balena inc.
"""
import requests
import os
import sys
import json
import traceback

from cloudevents.sdk.event import v1
from dapr.ext.grpc import App, BindingRequest
from dapr.clients import DaprClient

# remote (cloud) components, to be discovered
remote_components = []
# secret store components; value indicates if installed
secret_component_map = {'aws-secrets-manager': False, 'gcp-secret-manager': False,
                        'azure-keyvault': False}
# local components; value indicates if installed
local_component_map = {'local-mqtt': False}
# topic names for local MQTT component; blank if not defined
local_mqtt_topic_map = {'out': os.getenv('RELAY_OUT_TOPIC', ''),
                        'in': os.getenv('RELAY_IN_TOPIC', '')}

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
local_publish_url = f'http://localhost:{dapr_port}/v1.0/publish/local-mqtt/{local_mqtt_topic_map["in"]}?metadata.rawPayload=true'

app = App()
dc = DaprClient()

def find_components():
    """Build list of remote components from all components configured with dapr.
    
    :return: List of components found
    """
    components = []
    try:
        response = requests.get(f"http://localhost:{dapr_port}/v1.0/metadata")
        # print("components found " + str(response.content), flush=True)
        response_json = json.loads(response.content)

        for component in response_json["components"]:
            name = component['name']
            if name in local_component_map:
                local_component_map[name] = True
                print(f"Found local component {name}")
            elif name in secret_component_map:
                secret_component_map[name] = True
                print(f"Found secret component {name}")
            else:
                components.append(name)
                print(f"Found remote component {name}")

        # setup incoming event/data handlers
        if local_component_map['local-mqtt'] and local_mqtt_topic_map['out']:
            app._servicer.register_topic('local-mqtt', local_mqtt_topic_map['out'],
                                         local_subscribe, {'rawPayload': 'true'})
            print(f"Registered relay outbound handler for local MQTT component")
        if local_component_map['local-mqtt'] and local_mqtt_topic_map['in']:
            for name in components:
                app._servicer.register_binding(name, remote_binding)
                print(f"Registered relay inbound handler for remote component {name}")
    except Exception as e:
        print(f"Error parsing components: {e}")
        traceback.print_exc(file=sys.stdout)

    return components

def send_request(data):
    """Sends data to all remote components."""
    try:
        for component in remote_components:
            response = dc.invoke_binding(component, 'create', data)
            if response.text():
                print(f"Forwarded data to remote {component} with response {response.text()}")
            else:
                print(f"Forwarded data to remote {component}")
    except Exception as e:
        print(e, flush=True)

def local_subscribe(event: v1.Event) -> None:
    """Receives event/data from local component and forwards to remotes."""
    data = str(event.Data(), encoding='utf-8')
    print(f"Data received from local: {data}")
    send_request(data)

def remote_binding(request: BindingRequest):
    """Receives event/data from a remote component and forwards to local.
    """
    data = request.text()
    print(f"Data received from remote: {data}")
    # DaprClient should accept publish event with rawPayload metadata on daprd v1.2.2,
    # but the call fails. So must use HTTP request.
    #response = dc.publish_event(pubsub_name='local-mqtt', topic_name=relay_in_topic,
    #                            metadata=(('rawPayload', 'true')), data=request.text())
    response = requests.post(local_publish_url, data=data)
    print(f"Forwarded data to local with response {response}")


print("Data Relay block ==> run dapr and relay data to/from cloud")
remote_components = find_components()
app.run(50051)
