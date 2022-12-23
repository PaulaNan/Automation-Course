from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# by name
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
#
# first_name = chrome.find_element(By.NAME, 'firstname')
# first_name.send_keys('Marin')
#
# last_name = chrome.find_element(By.NAME, 'lastname')
# last_name.send_keys('Marina')
#
# continent = chrome.find_element(By.NAME, 'continents')
# continent.send_keys('Europe')
#
# # by id
# chrome.find_element(By.ID, 'datepicker').send_keys('11.12.2022')
#
# sleep(3)
# chrome.quit()
#
# chrome.maximize_window()
# chrome.get('https://phptravels.net/')
# chrome.find_element(By.ID, 'autocomplete').send_keys('Henri Coanda')
# chrome.find_element(By.CLASS_NAME, 'autocomplete-location').click()
# chrome.find_element(By.ID, 'autocomplete2').send_keys('CLuj Napoca')
# chrome.find_element(By.CLASS_NAME, 'autocomplete-location').click()
#
# # by class
# chrome.find_element(By.CLASS_NAME, 'depart form-control').send_keys('25-12-2022')
#
# sleep(3)
# chrome.quit()
#
#
# # # by name
# chrome.maximize_window()
# chrome.get('https://jules.app/sign-in')
#
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your email"]').send_keys('calin_paula@yahoo.com')
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your password"]').send_keys('maineninge')
# # chrome.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#
# chrome.maximize_window()
# chrome.get('https://www.emag.ro/')
# chrome.find_element(By.CSS_SELECTOR, 'input[id="searchboxTrigger"]').send_keys('telefon mobil')
# chrome.find_element(By.CSS_SELECTOR, 'i[class="em em-search"]').click()
# chrome.find_element(By.CSS_SELECTOR, 'button[data-option-id="31227"]').click()
# chrome.find_element(By.CSS_SELECTOR, 'span[class="filter-name"]').click()
# chrome.find_element(By.CSS_SELECTOR, 'a[data-name="Apple"]').click()
# chrome.find_element(By.CSS_SELECTOR, 'div[classe="Model"]').click()
# chrome.find_element(By.CSS_SELECTOR, 'a[data-name="iPhone 14 Pro"]').click()
#
#
# sleep(3)
# chrome.quit()

# x-path

chrome.maximize_window()

# navigate to url
chrome.get('https://the-internet.herokuapp.com/')
# chrome.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[1]/a[@href="/abtest"]').click()
# chrome.find_element(By.XPATH, '//a[text()="Dropdown"]').click()
# chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/select/option[3]').click()
chrome.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[21]/a[@href="/login"]').click()
chrome.find_element(By.XPATH, '//*[@id="username"]').send_keys('tomsmith')
chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/form/button/i').click()
chrome.find_element(By.XPATH, '/html/body/div[2]/div/div/a/i').click()
sleep(3)
chrome.quit()
