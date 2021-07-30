import os

NAME = "Local MQTT"
TYPE = "local"
FILE = "LocalMqtt.yaml"
VARS = [
    "LOCAL_MQTT_HOST",
    "RELAY_OUT_TOPIC",
]

def invoke():
    if os.getenv("LOCAL_MQTT_HOST") is None:
        print("Setting local MQTT host to the default: mqtt://localhost:1883")
        os.environ["LOCAL_MQTT_HOST"] = "mqtt://localhost:1883"

    if os.getenv("RELAY_OUT_TOPIC") is None:
        print("Setting relay outbound topic to the default: relay-out")
        os.environ["RELAY_OUT_TOPIC"] = "relay-out"
