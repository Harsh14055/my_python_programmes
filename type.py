from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
import random
import sys
import psutil  # To check and kill lingering Chrome processes

# Set Chrome profile path
chrome_profile_path = r"C:\Users\Dell\AppData\Local\Google\Chrome\User Data"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={chrome_profile_path}")  # Use your Chrome profile
chrome_options.add_argument("--profile-directory=Profile 3")  # Ensure correct profile

# Bypass bot detection flags
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

# Start Chrome with WebDriverManager (auto-downloads correct version)
driver = None

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open MonkeyType
    driver.get("https://monkeytype.com")

    # Wait for page load
    time.sleep(5)

    # Remove navigator.webdriver to bypass bot detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    # Locate the input box
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    print("Input box found!")

    # Locate and extract words dynamically
    words_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "word"))
    )
    words = [word.text for word in words_elements]

    # Wait for user to focus on the browser
    print("Switch to the browser within 5 seconds...")
    time.sleep(5)

    # **Human-like typing with random delays**
    for word in words:
        pyautogui.typewrite(word, interval=random.uniform(0.07, 0.15))  # Randomized typing speed
        pyautogui.typewrite(" ", interval=random.uniform(0.05, 0.12))  # Randomized space key delay

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # **Ensure Chrome fully quits**
    if driver:
        driver.quit()
        time.sleep(2)  # Allow time for Chrome to exit

    # **Kill lingering Chrome processes**
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        try:
            if "chrome" in proc.info["name"].lower():
                print(f"Killing process: {proc.info['name']} (PID: {proc.info['pid']})")
                psutil.Process(proc.info["pid"]).terminate()
        except psutil.NoSuchProcess:
            pass

    print("All processes closed successfully. Exiting.")
    sys.exit(0)
