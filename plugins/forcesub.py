import os
import sys
import asyncio

from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from database.database import add_1, add_2, add_3
from config import OWNER_ID

async def restart_bot(client: Bot, message: Message):
    await message.reply_text("BOT RESTARTING")
    await asyncio.sleep(1)  # Give some time for the message to be sent
    os.execv(sys.executable, ['python'] + sys.argv)

@Bot.on_message(filters.command("forcesub1"))
async def force_subscribe_command_1(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("Only the Owner can use this command, sorry!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>Incorrect format. Use the command like this:</b> /forcesub1 {channel_id}")
        return

    try:
        channel_id = int(message.command[1])
    except ValueError:
        await message.reply_text("Invalid channel ID. Please check again!")
        return

    # Add the new channel ID
    await add_1(channel_id)
    await message.reply_text(f"Channel ID {channel_id} has been set for Forcesub 1.")
    
    # Restart the bot with notification
    await restart_bot(client, message)

@Bot.on_message(filters.command("forcesub2"))
async def force_subscribe_command_2(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("Only the Owner can use this command, sorry!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>Incorrect format. Use the command like this:</b> /forcesub2 {channel_id}")
        return

    try:
        channel_id = int(message.command[1])
    except ValueError:
        await message.reply_text("Invalid channel ID. Please check again!")
        return

    # Add the new channel ID
    await add_2(channel_id)
    await message.reply_text(f"Channel ID {channel_id} has been set for Forcesub 2.")
    
    # Restart the bot with notification
    await restart_bot(client, message)

@Bot.on_message(filters.command("forcesub3"))
async def force_subscribe_command_3(client: Bot, message: Message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        await message.reply_text("Only the Owner can use this command, sorry!")
        return

    if len(message.command) != 2:
        await message.reply_text("<b>Incorrect format. Use the command like this:</b> /forcesub3 {channel_id}")
        return

    try:
        channel_id = int(message.command[1])
    except ValueError:
        await message.reply_text("Invalid channel ID. Please check again!")
        return

    # Add the new channel ID
    await add_3(channel_id)
    await message.reply_text(f"Channel ID {channel_id} has been set for Forcesub 3.")
    
    # Restart the bot with notification
    await restart_bot(client, message)
