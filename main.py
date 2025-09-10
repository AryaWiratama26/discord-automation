from dotenv import load_dotenv
import os
from automation import DiscordAutomation

# Load from .env
load_dotenv()
EMAIL_AKUN = os.getenv('EMAIL_AKUN')
PASSWORD_AKUN = os.getenv('PASSWORD_AKUN')
URL_LOGIN = os.getenv('URL_LOGIN')

# Data Message
data = ["Good Morning", "Guten Morgen", "Goedemorgen"]

# Jalankeun
bot_automation = DiscordAutomation(URL_LOGIN, EMAIL_AKUN, PASSWORD_AKUN)
bot_automation.login()
bot_automation.choose_server_and_send_message(server="testing", channel="test", data_message=data)
