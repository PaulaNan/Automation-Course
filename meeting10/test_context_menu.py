import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class ContextMenu(unittest.TestCase):
    CONTEXT = (By.XPATH, '//a[text()="Context Menu"]')
    BOX = (By.ID, 'hot-spot')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get('https://the-internet.herokuapp.com/')

    def test_context(self):
        self.chrome.find_element(*self.CONTEXT).click()
        # action chains helps us to wright click
        action = ActionChains(self.chrome)
        action.context_click(self.chrome.find_element(*self.BOX)).perform()
        sleep(3)
        # the command to click on alerts
        self.chrome.switch_to.alert.accept()

    def tearDown(self) -> None:
        self.chrome.quit()
        