from selenium import webdriver
from selenium.webdriver.common.by import By
import re
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
#for part in sorted_parts:
    #print(part)

for parts in links:
    parts.click()
    #print("Clicked")
    break

driver.switch_to.window(driver.window_handles[1])
print("Now In 2nd Page")
time.sleep(10)
download_bt = driver.find_elements(By.ID, 'method_free')
if download_bt:
    download_bt[0].click()
else:
    print("Download button not found")

driver.switch_to.window(driver.window_handles[2])
try:
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(5)
    driver.close()
    print("Page closed")
except IndexError:
    print("No page found")

driver.switch_to.window(driver.window_handles[1])
button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'bg-blue-600')]")
button.click()

try:
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(5)
    driver.close()
    print("Page closed")
except IndexError:
    print("No page found")

driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
buttondl = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'bg-blue-600')]")
buttondl.click()
