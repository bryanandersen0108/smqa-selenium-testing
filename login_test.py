import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    driver.find_element(By.ID, "login-button").click()

    title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert "inventory.html" in driver.current_url, "Incorrect URL"
    assert title.text == "Products", "Products page not found"

    print("Test Case: Successful Login")
    print("Expected Result: Products page is displayed")
    print("Actual Result: " + title.text)
    print("Test Result: PASSED")

    driver.save_screenshot("login_success.png")

except Exception as e:
    print("Test Result: FAILED")
    print("Error:", e)
    raise

finally:
    input("Press Enter to close the browser...")
    driver.quit()