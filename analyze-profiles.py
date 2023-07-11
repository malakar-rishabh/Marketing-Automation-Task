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

#select on the network button
my_network_url = 'https://www.linkedin.com/mynetwork/'
driver.get(my_network_url)
time.sleep(2)

#select on the see all button
see_all_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'See all')))
see_all_button.click()

#Gathering all the information of the connections one by one
connections = driver.find_elements(By.XPATH, "//li[contains(@class, 'mn-connection-card')]")
for connection in connections:
    connection.click()
    driver.switch_to.window(driver.window_handles[-1])  # Switch to the newly opened profile tab

    # Wait for the profile information to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'pv-top-card')))

    # Extract the name and headline from the profile
    name_element = driver.find_element(By.CLASS_NAME, 'pv-top-card--list')
    name = name_element.find_element(By.TAG_NAME, 'li').text

    headline_element = driver.find_element(By.CLASS_NAME, 'text-body-medium')
    headline = headline_element.text

    # Close the profile tab and switch back to the connections page
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
