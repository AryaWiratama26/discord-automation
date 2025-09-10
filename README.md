# discord-automation


```python

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

"""
Parameter:
 - server : Name of Server
 - channel : Name of Channel
 - data_message : List of message
"""

bot_automation.choose_server_and_send_message(server="testing", channel="test", data_message=data)

"""
Parameter:
 - server : Name of Server
 - voice_name : Name of voice chat
"""

bot_automation.voice_chat(server="testing", voice_name="MajuTakGentarMembelaYangBenar")


```


[Source Code](/automation/bot.py) </br>
[Env Example](.env.example) </br>
[Demo Video](https://youtu.be/N1kN4YcgRMw)