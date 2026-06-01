from selenium import *
from selenium.webdriver.chrome.service import *
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import *
import time
import sys

# Replace these with your LinkedIn login credentials
LINKEDIN_EMAIL = "Viplavreddychennupalli@gmail.com"
LINKEDIN_PASSWORD = "Hanuma@1102"


def init_driver():
    chrome_options = Options()
    # Uncomment if you want to run headless (no browser UI)
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()  # if chromedriver is in PATH, else pass executable_path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def login_to_linkedin(driver):
    try:
        driver.get("https://www.linkedin.com/login")
        wait = WebDriverWait(driver, 20)

        email_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        email_input.clear()
        email_input.send_keys(LINKEDIN_EMAIL)
        password_input.clear()
        password_input.send_keys(LINKEDIN_PASSWORD)
        login_button.click()

        # Wait until the Jobs icon or home page element loads to confirm login success
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/jobs')]")))

        print("✅ Logged in successfully.")
    except Exception as e:
        driver.save_screenshot("linkedin_login_error.png")
        print(f"❌ Login failed. Reason: {e}")
        driver.quit()
        sys.exit(1)


def search_jobs(driver, job_title="Software Engineer"):
    try:
        wait = WebDriverWait(driver, 20)

        # Navigate to the LinkedIn Jobs page directly
        driver.get("https://www.linkedin.com/jobs/?")

        # Wait for the job search input box
        search_input = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Search jobs')]"))
        )
        search_input.clear()
        search_input.send_keys(job_title)

        # Click on the search button (magnifying glass)
        search_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Search')]")
        search_button.click()

        # Wait a few seconds for results to load
        time.sleep(10)

        print(f"✅ Job search for '{job_title}' completed.")
    except Exception as e:
        driver.save_screenshot("linkedin_search_error.png")
        print(f"❌ Job search failed. Reason: {e}")
        driver.quit()
        sys.exit(1)


def main():
    driver = init_driver()

    login_to_linkedin(driver)

    # Optional: Pause here if manual CAPTCHA or 2FA is needed
  #  input("⏸️ If any CAPTCHA or 2FA is present, complete it now and press ENTER to continue...")

    search_jobs(driver, "Software Engineer")

    # Keep browser open for inspection, or quit
    print("✅ Script finished. Closing browser in 15 seconds...")
    time.sleep(15)
    driver.quit()


if __name__ == "__main__":
    main()
