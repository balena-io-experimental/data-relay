import os, json
import paho.mqtt.client as mqtt
from datetime import datetime
import time

client = mqtt.Client()
while True:
    client.connect("localhost", 1883, 60)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("Sending " + str(date_time))
    msgInfo = client.publish('cloud-input', date_time, 0, False)
    if False == msgInfo.is_published():
        msgInfo.wait_for_publish()
    client.disconnect()
    time.sleep(30)