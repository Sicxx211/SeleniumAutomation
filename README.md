# Automation with Selenium



# The idea behind it 

This is the first thing I have tried with Selenium, in the next days Im going to try even more things and im going to update this page once I have something more complex, until then I have this automation test that basically access the specified url, find a textbox where it will write whatever I input and press the send button.Fast and simple.


# The code 


from selenium import webdriver <br>
from selenium.webdriver.chrome.service import Service <br>
from selenium.webdriver.common.by import By <br>
import time <br> 
service = Service(executable_path='./chromedriver') <br>
chrome_browser = webdriver.Chrome(service=service) <br>
chrome_browser.maximize_window() <br>
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html') <br>
<br>
assert 'Selenium Easy Demo' in chrome_browser.title <br>
assert 'Show Message' in chrome_browser.page_source <br>
<br>
#This is how we grab the input field of the browser and type something inside it <br>
input_text = chrome_browser.find_element(By.ID, 'user-message') <br>
input_text.clear() <br>
input_text.send_keys('Automated message engaged!') <br>
<br>
#This will slow things a little bit so the browser won't detect the selenium automation as a robot <br>
time.sleep(2) <br>

#This is how we grab the button on the page and actually click it <br>
show_message_button = chrome_browser.find_element(By.CLASS_NAME,'btn-default') <br>
show_message_button.click() <br>
<br>
#This is how we grab the message that's being output after we click the button <br>
output_message = chrome_browser.find_element(By.ID,'display') <br>
assert 'Te iubesc mult de tot gogosica mea!' in output_message.text <br>
<br>
chrome_browser.quit() #Is going to completely close the chrome driver so all the session gets closed
