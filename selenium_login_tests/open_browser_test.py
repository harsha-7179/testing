from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Since chromedriver.exe is in the same folder, we can just use its name
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# --- THIS IS THE LINK YOU CHANGE ---
# I've put your LazyIntern URL here
driver.get("https://lazyintern-new-470415.uc.r.appspot.com/")

# We'll print messages to the terminal to see progress
print("Browser opened and went to the URL...")

driver.maximize_window()

# Wait for 5 seconds to observe
time.sleep(5)

driver.quit()

print("Browser closed. Test finished so fast .")

