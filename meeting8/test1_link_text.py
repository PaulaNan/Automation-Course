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
chrome.get('https://formy-project.herokuapp.com/')

# selector by link text
# chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
chrome.find_element(By.LINK_TEXT, 'Buttons').click()

sleep(3)
chrome.quit()
