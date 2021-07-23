import os

NAME = "Local MQTT"
TYPE = "local"
FILE = "LocalMqtt.yaml"
VARS = [
    "LOCAL_MQTT_HOST",
    "LOCAL_MQTT_INPUT_TOPIC",
]

def invoke():
    if os.getenv("LOCAL_MQTT_HOST") is None:
        print("Setting local MQTT host to the default: mqtt://localhost:1883")
        os.environ["LOCAL_MQTT_HOST"] = "mqtt://localhost:1883"

    if os.getenv("LOCAL_MQTT_INPUT_TOPIC") is None:
        print("Setting local MQTT input topic to the default: cloud-input")
        os.environ["LOCAL_MQTT_INPUT_TOPIC"] = "cloud-input"
