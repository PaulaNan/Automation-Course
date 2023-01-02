import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Alerts(unittest.TestCase):
    ALERT = (By.XPATH, '//button[text()="Click for JS Alert"]')
    CONFIRM = (By.XPATH, '//button[text()="Click for JS Confirm"]')
    PROMPT = (By.XPATH, '//button[text()="Click for JS Prompt"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get('https://the-internet.herokuapp.com/javascript_alerts')

    def test_alert(self):
        self.chrome.find_element(*self.ALERT).click()
        # switch the control to the alert window
        obj = self.chrome.switch_to.alert
        # retrieve the message on the alert window
        msg = obj.text
        print('Alert shows following message: ' + msg)
        sleep(3)
        # use the accept() method to accept the alert
        obj.accept()
        print('Clicked on tje OK button in the alert window')

    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM).click()
        # switch the control to the confirm window
        obj = self.chrome.switch_to.alert
        # retrieve the message on the confirm window
        message = obj.text
        print('Alert shows following message: ' + message)
        sleep(3)
        # use the accept() method to accept the confirm
        obj.accept()
        print('Clicked on the OK button in the comfirm window')
        sleep(3)

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM).click()
        # switch the control to the confirm window
        obj = self.chrome.switch_to.alert
        # retrieve the message on tje confirm window
        message = obj.text
        print('Confirm shows following message: ' + message)
        sleep(3)

    def test_prompt(self):
        self.chrome.find_element(*self.PROMPT).click()
        # switch the control to the prompt window
        obj = self.chrome.switch_to.alert
        # retrieve the message on the prompt window
        message = obj.text
        print('Prompt shows the following message: ' + message)
        # Enter the text into the prompt using send_keys()
        obj.send_keys('Mara')
        # use the accept() method to accept prompt
        obj.accept()
        print('Clicked on the OK button in the prompt window')
        sleep(3)

    def tearDown(self) -> None:
        self.chrome.quit()
