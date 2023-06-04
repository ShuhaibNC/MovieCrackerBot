# Bot information
SESSION = 'Media_search'
API_ID = 3616787
API_HASH = 'e49f6597a66149243a7baf5df57c0337'
BOT_TOKEN = '2089178930:AAE2Bu6Y5hcgr8x0iw4xCFjSJ-Lk8CFMZzM'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False
IMDB = False
LONG_IMDB_DESCRIPTION = False
MAX_LIST_ELM = None
LOG_CHANNEL = int('-1001943920731')

# Admins, Channels & Users
ADMINS = [908673468]
CHANNELS = [int('-1001814699331')]
AUTH_USERS = []
AUTH_GROUPS = None
AUTH_CHANNEL = int('-1001598825315')

# MongoDB information
DATABASE_URI = "mongodb+srv://shuhaibnc:Shuhaib123@cluster0.jauwz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = 'Cluster0'
COLLECTION_NAME = 'Telegram_files'  # If you are using the same database, then use different collection name for each bot
IMDB_TEMPLATE = """
<b>🏷 Title</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
☀️ Languages : <code>{languages}</code>
👥 Cast : <code>{cast}</code>
📀 RunTime: {runtime} Minutes
📆 Release Info : {release_date}
🎛 Countries : <code>{countries}</code>"""
CUSTOM_FILE_CAPTION = """
<b>📝 File Name:</b> <code>{file_name}</code> 

<b>🧲 File Size:</b> <code>{file_size}</code>

<b>Join ➠➠ [@MovieCracker](https://t.me/MovieCrackerLinks)</b>
"""
PICS = "https://raw.githubusercontent.com/ShuhaibNC/MovieCrackerBot/master/IMG_20230603_122555_814.jpg"
P_TTI_SHOW_OFF = True
SINGLE_BUTTON = True
SPELL_CHECK_REPLY = True
SUPPORT_CHAT = "@MovieCrackerLinks"
UPSTREAM_REPO = "https://github.com/ShuhaibNC/MovieCracker"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
