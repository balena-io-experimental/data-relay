"""
Test app to push the current CPU temperature to MQTT every 30 seconds.
"""
import os
import paho.mqtt.client as mqtt
from datetime import datetime
import time

def get_cpu_temp():
    """
    Obtains the current value of the CPU temperature. Reads the temperature in
    the file /sys/class/thermal/thermal*/temp, where thermal* is some device
    specific name like 'thermal_zone0'. Favors a dir that ends with '0'; otherwise
    just uses the first directory found with a valid name.
    
    :returns: Current value of the CPU temperature if successful, zero value otherwise.
    :rtype: float
    """
    # Initialize the result.
    result = 0.0
    # The first line in this file holds the CPU temperature as an integer times 1000.
    # Read the first line and remove the newline character at the end of the string.
    topDir = '/sys/class/thermal'
    if not os.path.isdir(topDir):
        print("{} directory not found".format(topDir))
        return result

    with os.scandir(topDir) as it:
        for d in it:
            if d.is_dir() and d.name.startswith('thermal'):
                try:
                    with open(topDir + '/' + d.name + '/temp') as f:
                        #print("Found file: {}".format(f.name))
                        line = f.readline().strip()
                        if line.isdigit():
                            # Convert the string with the CPU temperature to a float
                            # in degrees Celsius.
                            temp = float(line) / 1000

                            if (d.name.endswith('0') or result == 0.0) and temp > 0.0:
                                #print("Using temp in dir: {}".format(d.name))
                                result = temp
                except:
                    # We don't care if the temperature file does not exist
                    # or any other error; we're just looking for any reasonable
                    # temperature value.
                    pass
    return result


client = mqtt.Client()
while True:
    client.connect("mqtt", 1883, 60)
    data = "{}, {}, {:.2f}".format(os.getenv('BALENA_DEVICE_UUID', '0000000')[:7],
                            datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
                            get_cpu_temp())

    #print("Sending " + str(now))
    msgInfo = client.publish('cpu_temp', data, 0, False)
    if False == msgInfo.is_published():
        msgInfo.wait_for_publish()
    client.disconnect()

    time.sleep(30)
