import os
import requests
from router import reboot_router
from time import sleep
import datetime

TIMEOUT = 15
CHECK_COOLDOWN = 30
CHECK_URL = "https://google.com"

def check_connection():
    try:
        request = requests.get(CHECK_URL, timeout=TIMEOUT)
        print("Connected to the Internet -", datetime.datetime.now())
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection -", datetime.datetime.now())
        return False

def monitor():
    while True:
        if not check_connection():
            reboot_router()
        sleep(CHECK_COOLDOWN)

if __name__ == "__main__":
    monitor()