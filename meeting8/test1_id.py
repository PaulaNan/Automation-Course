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

# selector by ID
first_name = chrome.find_element(By.ID, 'first-name')
first_name.send_keys('Paula')
last_name = chrome.find_element(By.ID, 'last-name')
last_name.send_keys('Color')
job_title = chrome.find_element(By.ID, 'job-title')
job_title.send_keys('manager')
chrome.find_element(By.ID, 'select-meniu')
job_title.send_keys(5)
chrome.find_element(By.ID, 'datepicker')
job_title.send_keys(12/25/2022)

sleep(3)
chrome.quit()
