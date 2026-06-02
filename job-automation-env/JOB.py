from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Define your login credentials
LINKEDIN_EMAIL = "enter you linkedin ID"
LINKEDIN_PASSWORD = "Pass"

# Job preferences
JOB_TITLE = "Data Engineer"
JOB_LOCATION = "United States"

def login_to_linkedin(driver):
    """Logs into LinkedIn"""
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    email_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    email_input.send_keys(LINKEDIN_EMAIL)
    password_input.send_keys(LINKEDIN_PASSWORD)
    login_button.click()
    time.sleep(3)

def search_jobs(driver):
    """Searches for jobs on LinkedIn"""
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(2)

    search_box = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search jobs')]")
    location_box = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search location')]")

    search_box.send_keys(JOB_TITLE)
    location_box.send_keys(JOB_LOCATION)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

def apply_to_jobs(driver):
    """Loops through job listings and applies where possible"""
    job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

    for job in job_cards[:5]:  # Apply to first 5 jobs (modify as needed)
        try:
            job.click()
            time.sleep(2)

            easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
            easy_apply_button.click()
            time.sleep(2)

            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            time.sleep(3)

            print("✅ Applied to a job successfully!")
        except:
            print("⚠️ Skipping this job (no Easy Apply).")
        time.sleep(2)

if __name__ == "__main__":
    # Setup WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        login_to_linkedin(driver)
        search_jobs(driver)
        apply_to_jobs(driver)
    finally:
        drive.rquit()
