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

# set implicitly waits in seconds
# selenium will search all elements for x seconds before throughout an error
chrome.implicitly_wait(5)

# navigate to url
chrome.get('https://formy-project.herokuapp.com/form')

# found elem
chrome.find_element(By.ID, 'first-name').send_keys('Ana')

# invalid id => NoSuchElementException
chrome.find_element(By.ID, 'last-name123').send_keys('Ana')
