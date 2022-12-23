from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initialize chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximize window
chrome.maximize_window()

# set implicitly waits in seconds
# selenium will search all elements for x seconds before throughout an error
chrome.implicitly_wait(1)

# navigate to url
chrome.get('https://formy-project.herokuapp.com/form')

# found elem
chrome.find_element(By.ID, 'first-name').send_keys('Ana')

# search for 10 sec the elem (refresh every 500ms)
last_name = WebDriverWait(chrome, 5).until(EC.presence_of_element_located(By.ID, 'last-name123'))
last_name.send_keys('s')
