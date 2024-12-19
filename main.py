from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
import os

#Difine New Download Folder
download_dir = r"C:\Users\Rajapazza\Downloads\pyhon_test"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
    print("Unable to find the folder, Created a new Folder")
else:
    print("Your download folder has been found")

#Set download preferences to specify the download folder
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}

url = input("Enter FitGirl-Repacks game url here : ")

#Automatically Browser Closes Error Fix
options = webdriver.ChromeOptions() 
options.add_experimental_option('detach', True)
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

#Define monitor the download folder for completed download
def wait_for_download(download_folder, timeout=1200):
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        files = os.listdir(download_folder)
        incomplete_files = [f for f in files if f.endswith('.crdownload')]
        
        if not incomplete_files:
            return True
        time.sleep(1)
    
    print("Download timed out.Try again please")
    return False

# Get game url
driver.get(url)

# Click the game parts dropdown
link = driver.find_element(By.CLASS_NAME, "su-spoiler-title")
link.click()

# Find downloadble parts link
links = driver.find_elements(By.XPATH, '//a[starts-with(@href, "https://datanodes.to/")]')

#Print game all parts
pattern = r'part(\d+)'
parts = []
for link in links:
    href = link.get_attribute("href")
    match = re.search(pattern, href)
    if match:
        parts.append((int(match.group(1)), f"Part {match.group(1).zfill(3)}"))
sorted_parts = [part[1] for part in sorted(parts)]
for part in sorted_parts:
    print(part)

# Download each parts, one by one
x = 0
for parts in links:
    parts.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(10)
    download_bt = driver.find_elements(By.ID, 'method_free')
    if download_bt:
        download_bt[0].click()
    else:
        print("Download button not found in page 2")

    driver.switch_to.window(driver.window_handles[2])
    try:
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
    except IndexError:
        print("No page found")

    driver.switch_to.window(driver.window_handles[1])
    button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'bg-blue-600')]")
    button.click()

    try:
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
    except IndexError:
        print("No page found")

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    buttondl = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'bg-blue-600')]")
    buttondl.click()
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    if wait_for_download(download_dir):
        pp = x+1
        print("Part", pp , "Downloaded")
    else:
        print("Download did not complete within the timeout period.")

print("Game All Parts Are Downloaded")