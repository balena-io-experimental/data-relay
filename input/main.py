import os, json
import paho.mqtt.client as mqtt
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    run = os.environ.get('RUN') or None
    if run == '1':
        print("Connected with result code "+str(rc))
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        client.publish('fin', date_time, 0, False)

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883, 60)

client.loop_forever()