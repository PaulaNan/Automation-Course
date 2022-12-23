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

# selector by css - ID
chrome.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('A')
chrome.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys('Forever')
job_title = chrome.find_element(By.CSS_SELECTOR, '#job-title')
job_title.send_keys('Tester')
job_title.clear()
# selector by css - class - only one if is multiple matches
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('na')

# selector by css - attribute = value
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys('For')

# selector by css - attribute =  partial value + parent => kid
chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="Enter last name"]').send_keys('ever')
chrome.find_element(By.CSS_SELECTOR, "div input[placeholder='Enter your job title']").send_keys('tester')
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder*=dd/mm/yyyy]').send_keys('12/25/2022')

sleep(3)
chrome.quit()
