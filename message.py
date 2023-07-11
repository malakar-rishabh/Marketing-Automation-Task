from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/home?original_referer=https%3A%2F%2Fwww.linkedin.com%2Ffeed%2F')
driver.maximize_window()
time.sleep(2)

#getting the login and password field
driver.find_element(By.XPATH,"//input[@name='session_key']").send_keys('rishabhmalakar27@gmail.com')
driver.find_element(By.XPATH,"//input[@name='session_password']").send_keys('95@Rishabh!')
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(20)

#searching for the person
driver.get('https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=379')
driver.find_element(By.XPATH,"//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']").click()
#sending the message

#clicking on the message button
all_buttons = driver.find_elements(By.TAG_NAME,"button")
message_buttons = [ btn for btn in all_buttons if btn.text == "Message"]
message_buttons[1].click()

#For multiple messages here we can use a for loop but now we are sending a single message

#sending the message
driver.find_element(By.CLASS_NAME,"msg-form__contenteditable").click()  #clicking on the message box
paragraph = driver.find_elements(By.TAG_NAME,"p")
paragraph[-9].send_keys("Hii, This messenge is sent by a bot.")
time.sleep(4)
driver.find_element(By.CLASS_NAME,"msg-form__send-button artdeco-button artdeco-button--1").click()  #clicking on the send button
time.sleep(1)


# close  the message box
driver.find_element(By.CLASS_NAME,"msg-overlay-bubble-header__control msg-overlay-bubble-header__control--new-convo-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view").click()
time.sleep(2)
driver.quit() #closing the browser

