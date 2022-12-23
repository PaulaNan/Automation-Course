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


class Test(unittest.TestCase):
    # write one time the elem from a page
    SUBMIT_BTN = (By.XPATH, '//a[@role="button"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first-name"]')
    MIDDLE_NAME_INPUT = (By.XPATH, '//input[@id="middle-name"]')

    # before every test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://formy-project.herokuapp.com/form')

    # after every test
    def tearDown(self):
        self.chrome.quit()

    # check url
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://formy-project.herokuapp.com/form'
        # expected value, actual value, message for error
        self.assertEqual(expected, actual, 'url is incorrect')

    # check title page
    def test_page_title(self):
        actual = self.chrome.title
        expected = 'Formy'
        self.assertEqual(expected, actual, 'page title is incorrect')

    # verify text on element (button, error message)
    def test_submit_btn_text(self):
        # * tuple unpacking - takes value from tuple and put an argument on function
        actual = self.chrome.find_element(*self.SUBMIT_BTN).text
        expected = 'Submit'
        self.assertEqual(expected, actual, 'Submit button text is incorrect ')

    # verify a visible element
    def test_elem_visible(self):
        elem = self.chrome.find_element(*self.SUBMIT_BTN)
        self.assertTrue(elem.is_displayed(), 'Submit button is not visible')

    # verify that element has an expected attribute
    def test_elem_attribute(self):
        actual = self.chrome.find_element(*self.SUBMIT_BTN).get_attribute('class')
        expected = 'btn btn-lg btn-primary'
        self.assertEqual(expected, actual, 'Submit btn href attribute is wrong')

    # verify that an element is present
    def test_elem_not_displayed(self):
        # that way is not working
        middle_name = self.chrome.find_element(*self.MIDDLE_NAME_INPUT)
        self.assertFalse(middle_name.is_displayed(), 'Mid name is visible')
        pass

    # verify that the element is not present v1
    def test_elem_not_displayed_v1(self):
        # verify that the list is empty
        middle_name = self.chrome.find_elements()
        self.assertTrue(len(middle_name)) == 0, 'Mid name is visible in a wrong way'

    # verify that element is not present in v2
    def test_elem_not_displayed_v2(self):
        # verify the NoSuchElement exception
        try:
            self.chrome.find_element(*self.MIDDLE_NAME_INPUT)
        except NoSuchElementException:
            pass

    # waits on url
    def test_url_waits(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        # wait for the ex url to change
        WebDriverWait(self.chrome, 5).until(EC.url_changes('https://formy-project.herokuapp.com/form'))
        # wait for the new url contains
        WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks'))
        # we wait for the new url to be exact
        WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://formy-project.herokuapp.com/thanks'))

        # if in 5 sec we are not on the correct url, can try
        try:
            WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks2'))
        except TimeoutException:
            self.assertTrue(False, 'I waited 5 sec, but url is not displayed or not shown correctly')

