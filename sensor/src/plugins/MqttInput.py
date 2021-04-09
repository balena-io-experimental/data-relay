import os

NAME = "MQTT input"
TYPE = "input"
FILE = "MqttInput.yaml"
VARS = [
    "MQTT_HOST",
    "MQTT_INPUT_TOPIC",
]

def invoke():
    if os.getenv("MQTT_HOST") is None:
        print("Setting MQTT host to the default: mqtt://localhost:1883")
        os.environ["MQTT_HOST"] = "mqtt://localhost:1883"

    if os.getenv("MQTT_INPUT_TOPIC") is None:
        print("Setting MQTT input topic to the default: cloud-input")
        os.environ["MQTT_INPUT_TOPIC"] = "cloud-input"