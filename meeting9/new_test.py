from time import sleep
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialize chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximize window
chrome.maximize_window()


class Test2(unittest.TestCase):
    # write one time the elem from a page
    CONTACT_US = (By.XPATH, '//a[text()="Contact us"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@id="submitMessage"]')
    ERROR_MESSAGE = (By.XPATH, '//ol/li')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://automationpractice.com/index.php') # start url
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.CONTACT_US).click()

    # after every test
    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://automationpractice.com/index.php2controller=contact'
        # expected value, actual value, message for error
        self.assertEqual(expected, actual, 'url is incorrect')

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'Contact us - My store'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_elem_visible(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click() # click on button
        elem = self.chrome.find_element(self.ERROR_MESSAGE) # save error as elem
        self.assertTrue(elem.is_displayed(), 'Submit button is not visible')


# sleep te obliga in test sa faci pauza
# implicit/ explicit cauta la fiecare jumatate de secunda si daca il gaseste trece mai departe
# implicit orice elem
# explicit un elem anume
# daca un elem nu e vizibil putem verifica prin len si try- except
