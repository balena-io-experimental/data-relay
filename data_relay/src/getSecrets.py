"""
Provides access to a secret store via dapr. Starts and manages a dapr process,
which provides HTTP access to the store.

Assumes daprd executable in same directory as currently running process.

Usage:
    * open()
    * read_value() -- as needed
    * close() -- Must terminate the daprd process!

Copyright 2021 balena inc.
"""
import time
import requests
import os
import subprocess
import sys
import time

# Used to retrieve a secret; must be configured when opening the store
secrets_url = ""

# Popen object for the daprd process, or None if not started
dapr = None

def open(url_name, component_directory, is_debug_logging):
    """Opens the secret store so values may be read. Starts dapr process.

    :param url_name: Segment of URL with the name configured for the secret store
    :return: True on successful open; False otherwise
    """
    global secrets_url, dapr
    dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
    secrets_url = "http://localhost:{}/v1.0/secrets/{}/".format(dapr_port, url_name)

    args = ['daprd', '--components-path', component_directory, '--app-id', 'data_relay_block']
    if is_debug_logging:
        args.extend(['--log-level', 'debug'])
    print("Starting daprd process")
    try:
        dapr = subprocess.Popen(args)
        time.sleep(3)
    except Exception as e:
        print("Error starting daprd: {}".format(e))
        return False
    return True

def close():
    """Terminates dapr process"""
    if dapr:
        print("Terminating daprd process")
        try:
            dapr.terminate()
            time.sleep(5)
        except Exception as e:
            print("Error terminating daprd: {}".format(e))
    else:
        print("daprd process not found; can't terminate it")


def read_value(secret_name):
    """Reads the value for the provided name in the secret store.

    :return: secret value or None if not found
    """
    value = None
    try:
        print("Looking for {}".format(secret_name))
        url = secrets_url + secret_name
        response = requests.get(url)
        json_data = response.json()

        if response.status_code != 200:
            if "message" in json_data and "StatusCode=404" in json_data["message"]:
                # Secret not found, we do not care
                pass
            else:
                # Any other failure - log the details
                print("Getting secret failed with status code {}".format(response.status_code))
                print("Response: {}".format(json_data))

        value = json_data[secret_name]

    except Exception as e:
        print("Error retrieving secret: {}".format(e))
    return value
