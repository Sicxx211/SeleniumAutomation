from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service = Service(executable_path='./chromedriver')
chrome_browser = webdriver.Chrome(service=service)
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
assert 'Show Message' in chrome_browser.page_source

#This is how we grab the input field of the browser and type something inside it
input_text = chrome_browser.find_element(By.ID, 'user-message')
input_text.clear()
input_text.send_keys('Automated message engaged!')

#This will slow things a little bit so the browser won't detect the selenium automation as a robot
time.sleep(2)

#This is how we grab the button on the page and actually click it
show_message_button = chrome_browser.find_element(By.CLASS_NAME,'btn-default')
show_message_button.click()

#This is how we grab the message that's being output after we click the button
output_message = chrome_browser.find_element(By.ID,'display')
assert 'Te iubesc mult de tot gogosica mea!' in output_message.text


#Sometimes selenium can get buggy with close or quit, you can actually write it twice so you can be sure it's working properly
# chrome_browser.close() #This is going to close the current window that we work on
# chrome_browser.quit() #Is going to completely close the chrome driver so all the session gets closed