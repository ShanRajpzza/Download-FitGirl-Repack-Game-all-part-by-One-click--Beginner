from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Automatically Browser Closes Error Fix
options = webdriver.ChromeOptions() 
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

#Site URL
driver.get('https://fitgirl-repacks.site/grand-theft-auto-v/') 

# Click the link
link = driver.find_element(By.CLASS_NAME, "su-spoiler-title")
link.click()

links = driver.find_elements(By.XPATH, '//a[starts-with(@href, "https://datanodes.to/")]')

# Print all the parts' hrefs
for link in links:
    print(link.get_attribute("href"))