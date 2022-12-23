from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initialize chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximize window
chrome.maximize_window()

# navigate to url
chrome.get('https://formy-project.herokuapp.com/form')

actual = chrome.current_url
expected = 'https://formy-project.herokuapp.com/form2'

assert actual == expected, f'INVALID URL: expected {expected}, but found {actual}'

print('Test passes')
