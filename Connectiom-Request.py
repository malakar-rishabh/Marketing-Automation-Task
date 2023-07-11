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
driver.find_element(By.XPATH,"//input[@name='session_key']").send_keys('Enter Your Email') #Enter your username of linkedin
driver.find_element(By.XPATH,"//input[@name='session_password']").send_keys('Enter Your Password') #Enter your password of linkedin
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)

#Connecting with the random person
driver.get('https://www.linkedin.com/search/results/people/?keywords=SDE%20at%20tcs&network=%5B%22S%22%5D&origin=FACETED_SEARCH&sid=wp%40')
time.sleep(2)
all_buttons = driver.find_elements(By.TAG_NAME,"button")
connect_buttons = [ btn for btn in all_buttons if btn.text == "Connect"]


for btn in connect_buttons:
    driver.execute_script("arguments[0].click();",btn)
    time.sleep(10)
    send = driver.find_element(By.XPATH,"//buttons[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();",send)
    time.sleep(2)

    #if someone setup the privacy then we have to click on the close button
    try:
        close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();",close)
        time.sleep(2)
    except:
        pass

    #if someone has already sent the request then we have to click on the close button
    try:
        close = driver.find_element(By.XPATH,"//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();",close)
        time.sleep(2)
    except:
        pass


'''
#searching for the particular person like someone who is working in TCS as SDE
driver.find_element(By.ID,"global-nav-typeahead")
driver.find_element(By.CLASS_NAME,"search-global-typeahead__input").send_keys("SDE at TCS",Keys.ENTER)
time.sleep(10)

#Getting all connection buttons
all_buttons = driver.find_elements(By.TAG_NAME,"button")
connect_buttons = [ btn for btn in all_buttons if btn.text == "Connect"]
connect_buttons[0].click()
time.sleep(10)

#clicking on the send now button
driver.find_element(By.ID,"ember805")
driver.find_element(By.CLASS_NAME,"artdeco-button__text").click()
time.sleep(2) '''



















