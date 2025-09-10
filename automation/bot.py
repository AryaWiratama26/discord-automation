from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
            
            email = WebDriverWait(DRIVER, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Email or Phone Number']"))
            )

            email.send_keys(self.email)

            password = WebDriverWait(DRIVER, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Password']"))
            )
            
            password.send_keys(self.password)

            button_login = WebDriverWait(DRIVER, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
            )

            button_login.click()
        
            # time.sleep(10)
            
            print("Gass")

        except Exception as e:
            print(f"Error Login {e}")
            DRIVER.close()
            
    def choose_server_and_send_message(self, server, channel):
        
        try:
            button_choose_server = WebDriverWait(DRIVER,20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-dnd-name='{}']".format(server)))
            )

            button_choose_server.click()
            

            
            channel_choose = WebDriverWait(DRIVER,20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='{} (text channel)']".format(channel)))
            )

            channel_choose.click()

            message_box = WebDriverWait(DRIVER,20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Message #{}'][contenteditable='true']".format(channel)))
            )
        
            for i in range(5):
                message_box.send_keys("HELLO its meee")
                message_box.send_keys(Keys.ENTER)
            
            time.sleep(5)
            
            print("Berhasil")
        except Exception as e:
            print(f"error choose server and send message {e}")
        

        