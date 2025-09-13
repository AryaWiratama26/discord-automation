# discord-automation

This project was created for learning automation using selenium.


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


"""
Parameter:
 - data_message = List of Message
 - friend_name = Name of Friend
"""

bot_automation.friend_chat(data_message=["Hello Otong", "Apa Kabar?", "Semoga baik ya"], friend_name="otong_bulog")

"""
Parameter:
 - templates = Choose the template you want : ['create_my_own', 'friends', 'gaming', 'study_group', 'school_grup']
 - sec_op = More about the server : ['for_a_club_or_community', 'for_me_and_friend']
 - server_name = Name of Server
"""

bot_automation.create_server(templates="create_my_own", sec_op="for_me_and_friend", server_name="TESTING15")

"""
Parameter:
 - link_invite = Invitation Link
"""

bot_automation.join_server(link_invite="https://discord.gg/WmYDsXzubX")

```


[Source Code](/automation/bot.py) </br>
[Env Example](.env.example) </br>
[Demo Video](https://youtu.be/-Z3PfUCn4yI)