import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6088218026:AAEI6-9t9D7cCOmG9c8kUvPALZ5vIxE5tXc")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20860620"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "25d2343b36fc5aea3604c6c50a8e2b59")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002213021629"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6199677027"))

# Port
PORT = os.environ.get("PORT", "8070")

# Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://madara:madara@cluster0.tjfuu1g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Madara")

# Force sub channel id, if you want enable force sub
FORCE_CHANNEL = int(os.environ.get("FORCE_CHANNEL", "-1002044619047"))
FORCE_CHANNEL2 = int(os.environ.get("FORCE_CHANNEL2", "-1002044619047"))
FORCE_CHANNEL3 = int(os.environ.get("FORCE_CHANNEL3", "-1002044619047"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Mainly add graph else telegraph link
START_PIC = os.environ.get("START_PIC", "https://envs.sh/nDg.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/nDg.jpg")

# Add your text according to you
HELP_TXT = "<b>Hi!\nI am a bot!\n\nMade for @Anime_Bloodline⚡</b>"
ABOUT_TXT = "<b>╔════════════⦿\n├⋗ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={6199677027}'>ઝꪋઝꪋઽꫝꪱ</a>\n├⋗ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n├⋗ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n├⋗ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://t.me/ShadowKakashi>File Store Bot</a>\n├⋗ Main Channel : <a href=https://t.me/Anime_Bloodline>Anime Bloodline</a>\n├⋗ Support Group : <a href=https://t.me/community_Weebs>Community Weebs</a>\n╚═════════════════⦿</b>"

# start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\nI am Madara Uchiha a file store bot Made for @Anime_Bloodline ⚡</b>")
try:
    ADMINS=[7179837246]
    for x in (os.environ.get("ADMINS", "7179837246").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Owner list does not contain valid integers.")

# Force sub message
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Sorry Dude You're Not Joined My Channel 😐</b>\n\n<b>So Please Join Our Update Channel To Continue Watching Your Favourite Animes ⚡")

# set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "​🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Anime_Bloodline"

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

# Hi There My Name is Jatin and if you like this repo make sure to give it a thumbs up and don't Remove my credit....ELSE YOUR MOM FUCKED BY ME🤧
