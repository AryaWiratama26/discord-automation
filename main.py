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
# bot_automation.choose_server_and_send_message(server="testing", channel="test", data_message=data)
# bot_automation.voice_chat(server="testing", voice_name="MajuTakGentarMembelaYangBenar")
# bot_automation.friend_chat(data_message=["Hello Otong", "Apa Kabar?", "Semoga baik ya"], friend_name="otong_bulog")
bot_automation.create_server(templates="create_my_own", sec_op="for_me_and_friend", server_name="TESTING15")

