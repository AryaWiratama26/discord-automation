from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"

OP = webdriver.ChromeOptions()
# OP.add_argument('--headless')  

service = Service(executable_path=CHROME_DRIVER_PATH)

DRIVER = webdriver.Chrome(service=service, options=OP)

class DiscordAutomation:
    def __init__(self, url_login, email, password):
        self.url_login = url_login
        self.email = email
        self.password = password
        
    def login(self):
        try:
            DRIVER.get(self.url_login)
            
            email = WebDriverWait(DRIVER, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Email or Phone Number']"))
            )

            email.send_keys(self.email)

            password = WebDriverWait(DRIVER, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Password']"))
            )
            
            password.send_keys(self.password)

            button_login = WebDriverWait(DRIVER, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
            )

            button_login.click()
            
            time.sleep(10)
            
            print("Gass")

        except Exception as e:
            print(f"Error Login {e}")
            DRIVER.close()

        