# import unittest
# import HtmlTestRunner
#
# from homework9 import Test
# from meeting10.alerts import Alerts
#
#
# class TestSuite(unittest.TestCase):
#
#     def test_suite(self):
#         smoke_test = unittest.TestSuite()
#         smoke_test.addTests([
#             unittest.defaultTestLoader.loadTestsFromTestCase(Test),
#             unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
#         ])
#         # object html type
#         runner = HtmlTestRunner.HTMLTestRunner(
#             combine_reports=True,
#             report_title='Test',
#             report_name='Smoke Test Result'
#         )
#
#         runner.run(smoke_test)
#
import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


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
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()

    def tearDown(self):
        self.driver.quit()

    def test_new_page(self):
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, 'new page is incorrect')

    def test_page_title(self):
        actual = self.driver.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    def test_login_title(self):
        actual = self.driver.find_element(*self.LOGIN_PAGE).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Login page is incorrect')

    def test_login_button(self):
        # * tuple unpacking - takes value from tuple and put an argument on function
        actual = self.driver.find_element(*self.LOGIN_BTN).text
        expected = 'Login'
        self.assertEqual(expected, actual, 'Login button text is incorrect')

    def test_elem_visible(self):
        elem = self.driver.find_element(*self.ELEMENT_DISPLAY)
        self.assertTrue(elem.is_displayed(), 'Elemental Selenium is not visible')
