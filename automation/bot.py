from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from typing import List
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
            
    def choose_server_and_send_message(self, server: str, channel: str, data_message: List[str]):
        
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
            
            if len(data_message) == 1:
                message_box.send_keys(data_message[0])
                message_box.send_keys(Keys.ENTER)
            elif len(data_message) > 1:
                for i in data_message:
                    message_box.send_keys(i)
                    message_box.send_keys(Keys.ENTER)
            
            time.sleep(5)
            
            print("Berhasil")
        except Exception as e:
            print(f"error choose server and send message {e}")
            
    def voice_chat(self, server: str, voice_name: str ="General"):
        
        try:
            button_choose_server = WebDriverWait(DRIVER,20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-dnd-name='{}']".format(server)))
            )

            button_choose_server.click()
            
            button_voice_chat = WebDriverWait(DRIVER, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label^='{} (voice channel)']".format(voice_name)))
            )
            
            button_voice_chat.click()

            time.sleep(5)

            print("Berhasil ges")
        except Exception as e:
            print(f"error voice chat {e}")
            
    def friend_chat(self, data_message: List[str], friend_name: str):
        
        try:
            select_friend = WebDriverWait(DRIVER, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='{} (direct message)']".format(friend_name)))
            )

            select_friend.click()
            
            
            message = WebDriverWait(DRIVER, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Message @{}']".format(friend_name)))
            )
            
            if len(data_message) == 1:    
                message.send_keys(data_message[0])
                message.send_keys(Keys.ENTER)
            elif len(data_message) > 1:
                for i in data_message:
                    message.send_keys(i)
                    message.send_keys(Keys.ENTER)


            time.sleep(5)
            print("Mantap")
            
        except Exception as e:
            
            print(f"error friend chat {e}")
        

        