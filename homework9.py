from time import sleep
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):
    # write one time the elem from a page
    FORM_AUTHENTICATION = (By.XPATH, '//a[@href="/login"]')
    LOGIN_BTN = (By.XPATH, '//div[2]/div/div/form/button/i')
    ELEMENT_DISPLAY = (By.XPATH, '//div/a[@ target="_blank"]')
    INVALID_USERNAME = (By.XPATH, '//div[@id="flash"]')
    USER_NAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    ERROR_MESSAGE = (By.XPATH, '//div/a[@class="close"]')
    LOGOUT_BTN = (By.XPATH, '//div/a[@class="button secondary radius"]')
    LOGIN_PAGE = (By.XPATH, '//div/h2[text()="Login Page"]')

    # before every test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION).click()

    def tearDown(self):
        self.chrome.quit()

    def test_new_page(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'new page is incorrect')

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_login_title(self):
        actual = self.chrome.find_element(*self.LOGIN_PAGE).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Login page is incorrect')

    def test_login_button(self):
        # * tuple unpacking - takes value from tuple and put an argument on function
        actual = self.chrome.find_element(*self.LOGIN_BTN).text
        expected = 'Login'
        self.assertEqual(expected, actual, 'Login button text is incorrect')

    def test_elem_visible(self):
        elem = self.chrome.find_element(*self.ELEMENT_DISPLAY)
        self.assertTrue(elem.is_displayed(), 'Elemental Selenium is not visible')

    def test_login_button_click(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()
        actual = self.chrome.find_element(*self.INVALID_USERNAME).text
        expected = 'Your username is invalid!\n×'
        self.assertEqual(expected, actual, 'Username invalid')

    def test_invalid_user(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('user')
        self.chrome.find_element(*self.PASSWORD).send_keys('1234')
        self.chrome.find_element(*self.LOGIN_BTN).click()
        actual = self.chrome.find_element(*self.INVALID_USERNAME).text
        expected = 'Your username is invalid!\n×'
        self.assertEqual(expected, actual, 'Username invalid')

    def test_login_error(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()
        self.chrome.find_element(*self.ERROR_MESSAGE).click()
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Error message is still displayed')

    def test_list(self):
        list = self.chrome.find_element(By.XPATH, '//label')
        actual = list[0].text
        expected = 'Username'
        self.assertEqual(actual, expected, 'user label is incorrect')
        actual2 = list[1].text
        expected2 = 'Password'
        self.assertTrue(actual2, expected2, 'password label is incorrect')

    def test_user(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BTN).click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(expected, actual, 'new page is incorrect')

    def test_correct_user(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BTN).click()
        actual = self.chrome.find_element(*self.INVALID_USERNAME).text
        expected = 'You logged into a secure area!\n×'
        self.assertEqual(expected, actual, 'Secure area invalid')

    def test_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BTN).click()
        self.chrome.find_element(*self.LOGOUT_BTN).click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'new page is incorrect')
