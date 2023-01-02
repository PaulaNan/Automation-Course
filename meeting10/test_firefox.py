from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()

driver.get('https://the-internet.herokuapp.com/login')
first_name = driver.find_element(By.ID, 'username')
first_name.send_keys('Maria')

sleep(3)
driver.quit()

# other browsers
# https://pypi.org/project/webdriver-manager/#use-with-firefox
# https://user:pass@the-internet.herokuapp.com/basic_auth - to authenticate on a page
