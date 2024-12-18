from selenium import webdriver
from selenium.webdriver.common.by import By
import re

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

pattern = r'part(\d+)'  # Capture the number for sorting
parts = []

for link in links:
    href = link.get_attribute("href")
    match = re.search(pattern, href)
    if match:
        parts.append((int(match.group(1)), f"Part {match.group(1).zfill(3)}"))  # Store as (number, formatted string)

# Sort parts numerically and extract the formatted strings
sorted_parts = [part[1] for part in sorted(parts)]

# Print the sorted parts
for part in sorted_parts:
    print(part)