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

# selector by class it is usefully when we want a list
chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Paula')
chrome.find_elements(By.CLASS_NAME, 'form-control')[1].send_keys('Nice')
chrome.find_elements(By.CLASS_NAME, 'form-control')[2].send_keys('manager')

sleep(3)
chrome.quit()
