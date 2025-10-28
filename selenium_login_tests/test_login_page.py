import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

os.environ['WDM_LOCAL'] = '1'

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

URL = "https://lazyintern-new-470415.uc.r.appspot.com/accounts/login/"
driver.get(URL)
driver.maximize_window()
print("Opened the login page.")

try:
    print("Starting test LOGIN-001: Verifying UI elements...")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    print("✔ Email field is visible.")
    
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
    print("✔ Password field is visible.")
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Login as Student')]")))
    print("✔ 'Login as Student' button is visible.")
    
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Forgot your password?')]")))
    print("✔ 'Forgot your password?' link is visible.")
    
    # --- Using the correct selector from your screenshot ---
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".google-btn")))
    print("✔ 'Login with Google' element is visible.")
    
    print("\n✅ TEST PASSED: All elements for LOGIN-001 were found.")

except Exception as e:
    print(f"\n❌ TEST FAILED: An element was not found or timed out. Error: {e}")

finally:
    print("--- TEST FINISHED ---")
    time.sleep(3)
    driver.quit()