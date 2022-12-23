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

# selector by x-path - attribute - value
chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('A')
chrome.find_element(By.XPATH, '//input[@id="last-name"]').send_keys('S')

# selector by x-path -* all elements that follows the rule
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('n')
chrome.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('i')

# selector by x-path navigate down - passes through all elements
chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('d')
chrome.find_element(By.XPATH, '//div/div/input[@id="last-name"]').send_keys('m')

# selector by x-path navigate down - skip tags look everything by input that follows rhe rule
chrome.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('y')
chrome.find_element(By.XPATH, '//form//input[@id="last-name"]').send_keys('a')

# selector by x-path select element from list - index starts from 1
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('n')

# selector by x-path - OR first one from found
s = chrome.find_element(By.XPATH, '//input[@id="last-name1"] | //input[@id="last-name2"] | //input[@id="last-name"]')

# delete value from input
s.clear()
s.send_keys('Siman')

# selector by X-path - depending on partial text + take the text near with text property
full_text = chrome.find_element(By.XPATH, '//a[contains(text()), "Sub")]').text
print(full_text)
assert full_text == 'Submit'

# selector by x-path - depending on visible text
chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()

# x, y - axis navigation
# parent up
# /elem_type - we get to child element
# with //elem_type -search through all descendants
# with parent::elem_type up
# you can go up with parent::(name of the parent) or * ( -30')
# following sibling - following-sibling::input (next brother at the same level)
# preceding sibling - preceding-sibling::strong (previous brother from the same level)
# //label[text()='First name']/parent::strong/following-sibling::input+preceding-sibling::strong


def formy_input_by_placeholder(placeholder_text, input_value):
    input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    input.click()
    input.send_keys(input_value)


def formy_input_by_label(label, input_value):
    my_input = chrome.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong+parent::div//input')
    my_input.clear()
    my_input.send_keys(input_value)


formy_input_by_placeholder('Enter first name', 'Andy')
formy_input_by_placeholder('Enter last name', 'Sima')

formy_input_by_label('Job title', 'Automation engineer')

sleep(3)
chrome.quit()

# practice www.julles.app forgot password
# //span[text()="Send email"]/parent::button
