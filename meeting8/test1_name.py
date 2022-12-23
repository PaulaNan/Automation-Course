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
chrome.get('http://seleniumframework.com/Practiceform/')

# selector by name
chrome.find_element(By.NAME, 'name').send_keys('Paula')
chrome.find_element(By.NAME, 'email').send_keys('blablaa@yahoo.com')
chrome.find_element(By.NAME, 'telephone').send_keys('00405566725')
chrome.find_element(By.NAME, 'country').send_keys('Romania')
chrome.find_element(By.NAME, 'company').send_keys('ABC Company')
chrome.find_element(By.NAME, 'message').send_keys('Happy birthday')
chrome.find_element(By.LINK_TEXT, 'Submit').click()


sleep(3)
chrome.quit()
