#### This Code Was Devloped By @AM_ROBOTS ####

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://telegram.dog/VK_LINKZ')
    START_TXT = environ.get("START_TXT", "𝙷𝙴𝙻𝙾 {}")
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✪ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href='https://telegram.dog/Abt_Mine'>𝚃𝙷𝙸𝚂 𝙿𝙴𝚁𝚂𝙾𝙽 😃</a>
✪ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: <a href='https://docs.pyrogram.com'>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>
✪ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✪ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✪ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙺𝙾𝚈𝙴𝙱
✪ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂: <a href='https://telegram.dog/Vk_Botz'>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>
✪ 𝙼𝙾𝚅𝙸𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: <a href='https://telegram.dog/VK_LINKZ'>𝚃𝙾𝚄𝙲𝙷 𝙷𝙴𝚁𝙴</a>"""
    SOURCE_TXT = """<b>💯 𝙽𝙾𝚃𝙴 👇:</b>
     
<b>𝚆𝙴 𝙰𝚁𝙴 𝙽𝙾𝚃 𝚃𝙷𝙴 𝙾𝚆𝙽𝙴𝚁 𝙾𝙵 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃'𝚂 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴.𝚈𝙾𝚄 𝙲𝙰𝙽 𝙵𝙸𝙽𝙳 𝚃𝙷𝙸𝚂 𝙰𝚂 𝙰𝙽 𝙿𝚄𝙱𝙻𝙸𝙲 𝚁𝙴𝙿𝙾 𝙸𝙽 𝙶𝙸𝚃𝙷𝚄𝙱.𝙰𝙻𝙻 𝚃𝙷𝙴 𝙲𝚁𝙴𝙳𝙸𝚃𝚂 𝙶𝙾𝙴𝚂 𝚃𝙷𝙴 𝚁𝙴𝚂𝙿𝙴𝙲𝚃𝙴𝙳 𝙾𝚆𝙽𝙴𝚁𝚂 𝚆𝙷𝙾 𝙼𝙰𝙳𝙴 𝚃𝙷𝙸𝚂 𝙰𝚆𝙴𝚂𝙾𝙼𝙴 𝚆𝙾𝚁𝙺.💌</b>

</b>WE ARE JUST MODIFIED THE ORIGINAL REPO AS PER OUR NEEDS.#THANKYOU</b>"""
    MANUELFILTER_TXT = """ ➤ 𝙷𝙴𝙻𝙿: <b>𝙵𝙸𝙻𝚃𝙴𝚁𝚂</b>
    
𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙷𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝚃𝙷𝙰𝚃 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴
<b>𝙽𝙾𝚃𝙴:</b>

✸ 𝙸 𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴.
✸ 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃.
✸ 𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙷𝙰𝚅𝙴 𝙰 𝙻𝙸𝙼𝙸𝚃 𝙾𝙵 64 𝙲𝙷𝙰𝚁𝙰𝙲𝚃𝙴𝚁𝚂.

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /filter - <code>𝙰𝙳𝙳 𝙰 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃</code>
✯ /filters - <code>𝙻𝙸𝚂𝚃 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙾𝙵 𝙰 𝙲𝙷𝙰𝚃</code>
✯ /del - <code>𝙳𝙴𝙻𝙴𝚃𝙴 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝙲𝙷𝙰𝚃</code>
✯ /delall - <code>𝙳𝙴𝙻𝙴𝚃𝙴 𝚃𝙷𝙴 𝚆𝙷𝙾𝙻𝙴 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃 (𝙲𝙷𝙰𝚃 𝙾𝚆𝙽𝙴𝚁 𝙾𝙽𝙻𝚈)</code>"""
    BUTTON_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙱𝚄𝚃𝚃𝙾𝙽𝚂</b>
    
𝙸 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙱𝙾𝚃𝙷 𝚄𝚁𝙻 𝙰𝙽𝙳 𝙰𝙻𝙴𝚁𝚃 𝙸𝙽𝙻𝙸𝙽𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂.

<b>𝙽𝙾𝚃𝙴:</b>

✸ 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝚂 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙱𝚄𝚃𝚃𝙾𝙽𝙴𝚂 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙽𝚈 𝙲𝙾𝙽𝚃𝙴𝙽𝚃, 𝚂𝙾 𝙲𝙾𝙽𝚃𝙴𝙽𝚃 𝙸𝚂 𝙼𝙰𝙽𝙳𝙰𝚃𝙾𝚁𝚈.
✸ 𝙸 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝙴𝙳𝙸𝙰 𝚃𝚈𝙿𝙴.
✸ 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚂𝙷𝙾𝚄𝙻𝙳 𝙱𝙴 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝙿𝙰𝚁𝚂𝙴𝙳 𝙰𝚂 𝙼𝙰𝚁𝙺𝙳𝙾𝚆𝙽 𝙵𝙾𝚁𝙼𝙰𝚃.

<b>𝚄𝚁𝙻 𝙱𝚄𝚃𝚃𝙾𝙽𝚂:</b>

<code>[Button Text](buttonurl:https://t.me/heart_recipe)</code>

<b>𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂:</b>
<code>[Button Text](buttonalert:𝚃𝙷𝙸𝚂 𝙸𝚂 𝙰𝙽 𝙰𝙻𝙴𝚁𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴)</code>"""
    AUTOFILTER_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁</b>
    
<b>𝙽𝙾𝚃𝙴:</b>

✰ 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙵 𝙸𝚃'𝚂 𝙿𝚁𝙸𝚅𝙰𝚃𝙴.
✰ 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙳𝙾𝙴𝚂𝙽'𝚃 𝙲𝙾𝙽𝚃𝙰𝙸𝙽𝚂 𝙲𝙰𝙼𝚁𝙸𝙿𝚂,𝙿𝙾𝚁𝙽 𝙰𝙽𝙳 𝙵𝙰𝙺𝙴 𝙵𝙸𝙻𝙴𝚂.
✰ 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙻𝙰𝚂𝚃 𝙼𝙴𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚀𝚄𝙾𝚃𝙴𝚂.

 𝙸'𝙻𝙻 𝙰𝙳𝙳 𝙰𝙻𝙻 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙼𝚈 𝙳𝙱"""
    CONNECTION_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂</b>
    
✯ 𝚄𝚂𝙴𝙳 𝚃𝙾 𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝙱𝙾𝚃 𝚃𝙾 𝙿𝙼 𝙵𝙾𝚁 𝙼𝙰𝙽𝙰𝙶𝙸𝙽𝙶 𝙵𝙸𝙻𝚃𝙴𝚁𝚂.
✯ 𝙸𝚃 𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙰𝚅𝙾𝙸𝙳 𝚂𝙿𝙰𝙼𝙼𝙸𝙽𝙶 𝙸𝙽 𝙶𝚁𝙾𝚄𝙿𝚂.
<b>𝙽𝙾𝚃𝙴:</b>

✸ 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙰 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽.
✸ 𝚂𝙴𝙽𝙳 <code>/connect</code> 𝙵𝙾𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙽𝙶 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙿𝙼.

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>
✯ /connect  - <code>𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙲𝙷𝙰𝚃 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙿𝙼</code>
✯ /disconnect  - <code>𝙳𝙸𝚂𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝙵𝚁𝙾𝙼 𝙰 𝙲𝙷𝙰𝚃</code>
✯ /connections - <code>𝙻𝙸𝚂𝚃 𝙰𝙻𝙻 𝚈𝙾𝚄𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
    
<b>𝙽𝙾𝚃𝙴:</b>

𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝚃𝙷𝙴 𝙴𝚇𝚃𝚁𝙰 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /id - <code>𝚃𝙾 𝙶𝙴𝚃 𝙸𝙳 𝙾𝙵 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙴𝙳 𝚄𝚂𝙴𝚁.</code>
✯ /info  - <code>𝙶𝙴𝚃 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙱𝙾𝚄𝚃 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /imdb  - <code>𝙶𝙴𝚃 𝚃𝙷𝙴 𝙵𝙻𝙸𝙼 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙵𝙾𝚁 𝙸𝙼𝙳𝙱 𝚂𝙾𝚄𝚁𝙲𝙴.</code>
✯ /search  - <code>𝙶𝙴𝚃 𝚃𝙷𝙴 𝙵𝙻𝙸𝙼 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙵𝚁𝙾𝙼 𝚅𝙰𝚁𝙸𝙾𝚄𝚂 𝚂𝙾𝚄𝚁𝙲𝙴𝚂.</code>"""
    ADMIN_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙰𝙳𝙼𝙸𝙽 𝙼𝙾𝙳𝚂</b>
    
<b>𝙽𝙾𝚃𝙴:</b>

𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝙰𝙳𝙼𝙸𝙽𝚂

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /logs - <code>𝚃𝙾 𝙶𝙴𝚃 𝚃𝙷𝙴 𝚁𝙴𝚂𝙲𝙴𝙽𝚃 𝙴𝚁𝚁𝙾𝚁𝚂</code>
✯ /stats - <code>𝚃𝙾 𝙶𝙴𝚃 𝚃𝙷𝙴 𝚂𝚃𝙰𝚃𝚄𝚂 𝙾𝙵 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙳𝙱.</code>
✯ /delete - <code>𝚃𝙾 𝙳𝙴𝙻𝙴𝚃𝙴 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙵𝙸𝙻𝙴 𝙵𝚁𝙾𝙼 𝙳𝙱.</code>
✯ /users - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝙼𝚈 𝚄𝚂𝙴𝚁𝚂 𝙰𝙽𝙳 𝙸𝙳𝚂.</code>
✯ /chats - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙷𝙴 𝙼𝚈 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙸𝙳𝚂.</code>
✯ /leave  - <code>𝚃𝙾 𝙻𝙴𝙰𝚅𝙴 𝙵𝚁𝙾𝙼 𝙰 𝙲𝙷𝙰𝚃.</code>
✯ /disable  -  <code>𝚃𝙾 𝙳𝙸𝚂𝙰𝙱𝙻𝙴 𝙰 𝙲𝙷𝙰𝚃.</code>
✯ /ban_user  - <code>𝚃𝙾 𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /unban_user  - <code>𝚃𝙾 𝚄𝙽𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /channel - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙾𝚃𝙰𝙻 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂.</code>
✯ /broadcast - <code>𝚃𝙾 𝙱𝚁𝙾𝙳𝙲𝙰𝚂𝚃 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙰𝙻𝙻 𝚄𝚂𝙴𝚁𝚂.</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝙶𝚁𝙾𝚄𝙿 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 ⪼ <code>{}</code></b>
<b>᚛› 𝙰𝙳𝙳𝙴𝙳 𝙱𝚈 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝙸𝙳 - <code>{}</code></b>
<b>᚛› 𝙽𝙰𝙼𝙴 - {}</b>
"""
