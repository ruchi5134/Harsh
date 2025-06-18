import asyncio

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait
from pyrogram.types import Message

import config
from SystemMusic.misc import SUDOERS
from SystemMusic import app, userbot


@app.on_message(filters.command(["leaveallone"]) & SUDOERS)
async def leaveall(_, message: Message):
    hm = await message.reply_text(f"» {userbot.one.name} sᴛᴀʀᴛᴇᴅ ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛs...")
    left = 0
    chats = []
    async for dialog in userbot.one.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            chats.append(int(dialog.chat.id))
    schat = (await app.get_chat(config.LOGGER_ID)).id
    for i in chats:
        if i in (config.LOGGER_ID, int(schat)):
            continue
        try:
            await userbot.one.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.value))
        except Exception:
            pass
    try:
        await hm.edit_text(
            f"<b>» {userbot.one.name} sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :</b>\n\n<b>ʟᴇғᴛ :</b> <code>{left}</code>"
        )
    except:
        pass


@app.on_message(filters.command(["leavealltwo"]) & SUDOERS)
async def leaveall(_, message: Message):
    hm = await message.reply_text(f"» {userbot.two.name} sᴛᴀʀᴛᴇᴅ ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛs...")
    left = 0
    chats = []
    async for dialog in userbot.two.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            chats.append(int(dialog.chat.id))
    schat = (await app.get_chat(config.LOGGER_ID)).id
    for i in chats:
        if i in (config.LOGGER_ID, int(schat)):
            continue
        try:
            await userbot.two.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.value))
        except Exception:
            pass
    try:
        await hm.edit_text(
            f"<b>» {userbot.two.name} sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :</b>\n\n<b>ʟᴇғᴛ :</b> <code>{left}</code>"
        )
    except:
        pass


@app.on_message(filters.command(["leaveallthree"]) & SUDOERS)
async def leaveall(_, message: Message):
    hm = await message.reply_text(f"» {userbot.three.name} sᴛᴀʀᴛᴇᴅ ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛs...")
    left = 0
    chats = []
    async for dialog in userbot.three.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            chats.append(int(dialog.chat.id))
    schat = (await app.get_chat(config.LOGGER_ID)).id
    for i in chats:
        if i in (config.LOGGER_ID, int(schat)):
            continue
        try:
            await userbot.three.leave_chat(int(i))
            left += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.value))
        except Exception:
            pass
    try:
        await hm.edit_text(
            f"<b>» {userbot.three.name} sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛs :</b>\n\n<b>ʟᴇғᴛ :</b> <code>{left}</code>"
        )
    except:
        pass
