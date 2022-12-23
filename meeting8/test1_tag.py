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

# selector by tag - for unique tag
chrome.find_element(By.TAG_NAME, 'input').send_keys("Andy")

# we find many and put then on a list. when use -s (elements) create a list to know what tag to call
input_list = chrome.find_elements(By.TAG_NAME, 'input')
input_list[1].send_keys('Maro')

sleep(3)
chrome.quit()
