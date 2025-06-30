from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def join_google_meet(meeting_url):
    options = Options()

    # Use your copied Chrome profile
    options.add_argument(r"user-data-dir=C:\\Users\\harsh\\AppData\\Local\\Google\\Chrome\\ChromBotProfile")
    options.add_argument("profile-directory=Default")

    # Optional but recommended flags
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--use-fake-ui-for-media-stream")  # Auto allow mic/cam
    options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid bot detection

    # Launch Chrome with the profile
    driver = webdriver.Chrome(options=options)

    # Open the meeting URL
    driver.get(meeting_url)

    time.sleep(5)  # Let page load

    try:
        join_button = driver.find_element(By.XPATH, "//button[contains(@jsname, 'Qx7uuf')]")
        join_button.click()
        print("✅ Auto-clicked Join button.")
    except Exception as e:
        print("❌ Could not auto-join. Please click 'Join' manually...")
        print("Error:", e)

    timeout = time.time() + 60
    while True:
        try:
            # This selector checks if muted button is present, meaning you joined
            driver.find_element(By.XPATH, "//div[@role='button' and @data-is-muted]")
            print("✅ In meeting.")
            break
        except:
            if time.time() > timeout:
                print("❌ Timeout waiting for join.")
                driver.quit()
                exit()
            time.sleep(2)

    return driver
