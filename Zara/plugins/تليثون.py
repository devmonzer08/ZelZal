#zein
from asyncio import sleep
import asyncio
import requests
import time
from telethon.tl import types
from telethon.tl.types import Channel, Chat, User, ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import ChannelPrivateError
from ..Config import Config
from telethon.errors import (
    ChatAdminRequiredError,
    FloodWaitError,
    MessageNotModifiedError,
    UserAdminInvalidError,
)
from telethon.tl import functions
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.channels import EditBannedRequest, LeaveChannelRequest
from telethon.tl.functions.channels import EditAdminRequest
from telethon import events
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantCreator,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
    InputPeerChat,
    MessageEntityCustomEmoji,
)
from Zara import zedub
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from datetime import datetime
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from ..core.logger import logging
from ..helpers.utils import reply_id
from ..sql_helper.locks_sql import *
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import readable_time
from . import BOTLOG, BOTLOG_CHATID
LOGS = logging.getLogger(__name__)
plugin_category = "admin"
spam_chats = []
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

async def ban_user(chat_id, i, rights):
    try:
        await zedub(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)        

# الكود من ابداع رشق
@zedub.zed_cmd(pattern=r"رشق(.*)")
async def hussein(event):
    await event.edit("**᯽︙ جارِ الجواب على سؤالك انتظر قليلاً ...**")
    text = event.pattern_match.group(1).strip()
    if text:
        response = requests.get(f'https://ava-tar.online/api/DR_CRISS/api.php?add={text}').text
        await event.edit(response)
    else:
        await event.edit("يُرجى كتابة رسالة مع الأمر للحصول على إجابة.")
is_Reham = False
No_group_Joker = "@V_P_N_8"
# يا يلفاشل هم الك نيه تاخذه وتنشره بسورسك 🤣
active_aljoker = []

@zedub.zed_cmd(pattern=r"الرشق تفعيل")
async def enable_bot(event):
    global is_Reham
    if not is_Reham:
        is_Reham = True
        active_aljoker.append(event.chat_id)
        await event.edit("**᯽︙ تم تفعيل امر الذكاء الاصطناعي سيتم الرد على اسئلة الجميع عند الرد علي.**")
    else:
        await event.edit("**᯽︙ الزر مُفعّل بالفعل.**")
@zedub.zed_cmd(pattern=r"الرشق تعطيل")
async def disable_bot(event):
    global is_Reham
    if is_Reham:
        is_Reham = False
        active_aljoker.remove(event.chat_id)
        await event.edit("**᯽︙ تم تعطيل امر الذكاء الاصطناعي.**")
    else:
        await event.edit("**᯽︙ الزر مُعطّل بالفعل.**")
@zedub.on(events.NewMessage(incoming=True))
async def reply_to_hussein(event):
    if not is_Reham:
        return
    if event.is_private or event.chat_id not in active_aljoker:
        return
    message = event.message
    if message.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.sender_id == event.client.uid:
            text = message.text.strip()
            if event.chat.username == No_group_Joker:
                return
            response = requests.get(f'https://ava-tar.online/api/DR_CRISS/api.php?add={text}').text
            await asyncio.sleep(4)
            await event.reply(response)
aljoker = False
async def aljoker_nshr(zedub, sleeptimet, chat, message, seconds):
    global aljoker
    aljoker = True
    while aljoker:
        if message.media:
            sent_message = await zedub.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await zedub.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
