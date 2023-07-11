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


#Compitator Linkedin Profile
competitor_profile_url = 'https://www.linkedin.com/in/competitor_profile' #You can enter any profile url of linkedin
driver.get(competitor_profile_url)
time.sleep(2)


#monitor the activity of the competitor
# Wait for the page to load and locate the container of the recent posts
posts_container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='occludable-update ember-view']")))

# Find all the posts
posts = posts_container.find_elements(By.XPATH, ".//div[@class='occludable-update ember-view']")

# Print the text content of each post
for post in posts:
    print(post.text)
