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

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '18080178'))
API_HASH = environ.get('API_HASH', 'ed8003bc110f89c314415faa79c953b4')
BOT_TOKEN = environ.get('BOT_TOKEN', '5809058677:AAEpOm-o8EPwe7qXpU_gRj1Xt3qL823TlQE')
PORT = environ.get("PORT", "8080")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/3504dae22b95edf9d7a34.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1396584367').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001634923998')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://reqnew:reqnew@cluster0.hvgu3fq.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Reqnew")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_filess')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001602598101))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'heart_recipe')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", """<code>{file_name}</code> 

<b>[𝙹𝙾𝙸𝙽 𝚄𝚂 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝚄𝙿𝙳𝙰𝚃𝙴𝚂..](https://t.me/VK_LINKZ)</b>""")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", """<b>🎞 𝚃𝙸𝚃𝚃𝙻𝙴</b>: <a href={url}>{title}</a>
<b>🎭 𝙶𝙴𝙽𝚁𝙴𝚂</b>: {genres}
<b>📆 𝚈𝙴𝙰𝚁</b>: <a href={url}/releaseinfo>{year}</a>
<b>🌟 𝚁𝙰𝚃𝙸𝙽𝙶</b>: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
<b>🎙 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴𝚂</b> : <code>{languages}</code>
<b>📀 𝚁𝚄𝙽𝚃𝙸𝙼𝙴</b>: {runtime} Minutes
<b>📆 𝚁𝙴𝙻𝙴𝙰𝚂𝙴 𝙸𝙽𝙵𝙾</b> : {release_date}
<b>🌀 𝙲𝙾𝚄𝙽𝚃𝚁𝙸𝙴𝚂</b> : <code>{countries}</code>

<b>📚𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 </b>: {message.from_user.mention}

<b>♻️𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙹𝙾𝙸𝙽 𝚄𝚂</b>: @VK_LINKZ""")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##

      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'dulink.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '8e228c9ad067f6580c498f797b38099b4baba774')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 300))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/how_2d_vk/4"

   # Custom Caption Under Button #
CAPTION_BUTTON = "Suscribe"
CAPTION_BUTTON_URL = "https://telegram.dog/VK_LINKZ"

   # Auto Delete For Bot Sending Files #
