import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6088218026:AAEI6-9t9D7cCOmG9c8kUvPALZ5vIxE5tXc")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23902408"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a36a4ef2f07d63aeba7b53b99c64d73")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002213021629"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7179837246"))

# Port
PORT = os.environ.get("PORT", "7070")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mex:rex@cluster7.jrzowqz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Chuuttiya")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002044619047"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002044619047"))
FORCE_CHANNEL3 = int(os.environ.get("FORCE_CHANNEL3", "-1002044619047"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/b1549fd4bc4a2b7dd04aa.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/3ab8716b37894ef7460e9.jpg")

# Add your text according to you
HELP_TXT = "<b>Hi!\nI am a bot!\n\nMade for @Anime_Bloodline⚡</b>"
ABOUT_TXT = "<b>Hi {first}!\n\n● ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/RarelySukuna>S U K U N A</a>\n● ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Anime_Bloodline>ᴀɴɪᴍᴇ Bloodlina</a>\n● ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Ongoing_Anime_Bloodline>ᴏɴɢᴏɪɴɢ Bloodline</a>\n● Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</b>"

# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - @Anime_Bloodline</b>")
try:
    ADMINS=[7179837246]
    for x in (os.environ.get("ADMINS", "7179837246").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Owner list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Movies_Series_Universe"

ADMINS.append(OWNER_ID)
ADMINS.append(7179837246)

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

LOG_FILE_NAME = "filesharingbot.txt"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Hi There My Name is Sahil and if you like this repo make sure to give it a thumbs up and don't Remove my credit....
