import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

ROUTER_IP = os.environ['TMOBILE_GATEWAY']
USER = os.environ['TMOBILE_USER']
PASSWORD = os.environ['TMOBILE_PASSWORD']

def reboot_router_task():
    print('trying to reboot router')

    try:
        # Using Chrome to access the gateway
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print('unable to connect to start chrome driver - check installation')
        return False

    try:
        driver.get('http://' + ROUTER_IP)
    except Exception as e:
        print('unable to connect to router')
        return False

    try:
        # click on the system button to open the login popup
        driver.find_element(by=By.LINK_TEXT, value='System').click()

        # input the username and password
        sleep(2)
        input_username = driver.find_element(by=By.XPATH, value='//input[@placeholder="Enter your Username"]')
        input_username.send_keys(USER)
        sleep(2)
        input_password = driver.find_element(by=By.XPATH, value='//input[@placeholder="Enter your Password"]')
        input_password.send_keys(PASSWORD)

        # login
        sleep(2)
        driver.find_element(by=By.ID, value='login-dialog-button-login').click()

        # click on restart
        sleep(3)
        driver.find_element(by=By.ID, value='restart').click()

        # confirm restart
        sleep(2)
        driver.find_element(by=By.CLASS_NAME, value='nokia-confirm__button').click()

        print('rebooted router')
        sleep(5)
        driver.close()
        return True
    except Exception as e:
        print(e)
    return False

def reboot_router():
    if reboot_router_task():
        print('sleeping for 10 minutes after reboot')
        sleep(600)
    else:
        print('sleeping for 5 minutes after reboot error')
        sleep(300)

if __name__ == "__main__":
    reboot_router()