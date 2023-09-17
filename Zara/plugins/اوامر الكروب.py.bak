#aljokrr
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
from HuRe import zedub
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
@zedub.on(events.NewMessage(outgoing=True, pattern="ارسل?(.*)"))
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("تم الارسال الرسالة الى الرابط الذي وضعتة")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("تم ارسال الرساله الى الرابط الذي وضعتة")
    except BaseException:
        await event.edit("** عذرا هذا ليست مجموعة **")
@zedub.zed_cmd(
    pattern="اطردني$",
    command=("اطردني", plugin_category),
    info={
        "header": "To kick myself from group.",
        "usage": [
            "{tr}kickme",
        ],
    },
    groups_only=True,
)
async def kickme(leave):
    "to leave the group."
    await leave.edit("᯽︙  حسنا سأغادر المجموعه وداعا ")
    await leave.client.kick_participant(leave.chat_id, "me")


@zedub.zed_cmd(pattern="مغادرة الكروبات")
async def Reda (event):
    await event.edit("**᯽︙ جارِ مغادرة جميع الكروبات الموجوده في حسابك ...**")
    gr = []
    dd = []
    num = 0
    try:
        async for dialog in event.client.iter_dialogs():
         entity = dialog.entity
         if isinstance(entity, Channel) and not entity.megagroup:
             continue
         elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
            ):
                 gr.append(entity.id)
                 if entity.creator or entity.admin_rights:
                  dd.append(entity.id)
        dd.append(188653089)
        dd.append(1629927549)
        for group in gr:
            if group not in dd:
                await zedub.delete_dialog(group)
                num += 1
                await sleep(1)
        if num >=1:
            await event.edit(f"**᯽︙ تم المغادرة من {num} كروب بنجاح ✓**")
        else:
            await event.edit("**᯽︙ ليس لديك كروبات في حسابك لمغادرتها !**")
    except BaseException as er:
     await event.reply(f"حدث خطأ\n{er}\n{entity}")

DevJoker = [6300938349]
@zedub.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("اطلع") and event.sender_id in DevJoker:
        message = event.message
        channel_username = None
        if len(message.text.split()) > 1:
            channel_username = message.text.split()[1].replace("@", "")
        if channel_username:
            try:
                entity = await zedub.get_entity(channel_username)
                if isinstance(entity, Channel) and entity.creator or entity.admin_rights:
                    response = "**᯽︙ لا يمكنك الخروج من هذه القناة. أنت مشرف أو مالك فيها!**"
                else:
                    await zedub(LeaveChannelRequest(channel_username))
                    response = "**᯽︙ تم الخروج من القناة بنجاح!**"
            except ValueError:
                response = "خطأ في العثور على القناة. يرجى التأكد من المعرف الصحيح"
        else:
            response = "**᯽︙ يُرجى تحديد معرف القناة أو المجموعة مع الخروج يامطوري ❤️**"
        #await event.reply(response)
        
@zedub.zed_cmd(pattern="مغادرة القنوات")
async def Hussein (event):
    await event.edit("**᯽︙ جارِ مغادرة جميع القنوات الموجوده في حسابك ...**")
    gr = []
    dd = []
    num = 0
    try:
        async for dialog in event.client.iter_dialogs():
         entity = dialog.entity
         if isinstance(entity, Channel) and entity.broadcast:
             gr.append(entity.id)
             if entity.creator or entity.admin_rights:
                 dd.append(entity.id)
        dd.append(1527835100)
        for group in gr:
            if group not in dd:
                await zedub.delete_dialog(group)
                num += 1
                await sleep(1)
        if num >=1:
            await event.edit(f"**᯽︙ تم المغادرة من {num} قناة بنجاح ✓**")
        else:
            await event.edit("**᯽︙ ليس لديك قنوات في حسابك لمغادرتها !**")
    except BaseException as er:
     await event.reply(f"حدث خطأ\n{er}\n{entity}")

@zedub.zed_cmd(pattern="تصفية الخاص")
async def hussein(event):
    await event.edit("**᯽︙ جارِ حذف جميع الرسائل الخاصة الموجودة في حسابك ...**")
    dialogs = await event.client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_user:
            try:
                await event.client(DeleteHistoryRequest(dialog.id, max_id=0, just_clear=True))
            except Exception as e:
                print(f"حدث خطأ أثناء حذف المحادثة الخاصة: {e}")
    await event.edit("**᯽︙ تم تصفية جميع محادثاتك الخاصة بنجاح ✓ **")

@zedub.zed_cmd(pattern="تصفية البوتات")
async def Hussein(event):
    await event.edit("**᯽︙ جارٍ حذف جميع محادثات البوتات في الحساب ...**")
    result = await event.client(GetContactsRequest(0))
    bots = [user for user in result.users if user.bot]
    for bot in bots:
        try:
            await event.client(DeleteHistoryRequest(bot.id, max_id=0, just_clear=True))
        except Exception as e:
            print(f"حدث خطأ أثناء حذف محادثات البوت: {e}")
    await event.edit("**᯽︙ تم حذف جميع محادثات البوتات بنجاح ✓ **")

# الكود من كتابة فريق الجوكر بس تسرقة تنشر بقناة الفضايح انتَ وقناتك 🖤
@zedub.zed_cmd(pattern=r"ذكاء(.*)")
async def hussein(event):
    await event.edit("**᯽︙ جارِ الجواب على سؤالك انتظر قليلاً ...**")
    text = event.pattern_match.group(1).strip()
    if text:
        response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
        await event.edit(response)
    else:
        await event.edit("يُرجى كتابة رسالة مع الأمر للحصول على إجابة.")
is_Reham = False
No_group_Joker = "@sourceav"
# يا يلفاشل هم الك نيه تاخذه وتنشره بسورسك 🤣
active_aljoker = []

@zedub.zed_cmd(pattern=r"الذكاء تفعيل")
async def enable_bot(event):
    global is_Reham
    if not is_Reham:
        is_Reham = True
        active_aljoker.append(event.chat_id)
        await event.edit("**᯽︙ تم تفعيل امر الذكاء الاصطناعي سيتم الرد على اسئلة الجميع عند الرد علي.**")
    else:
        await event.edit("**᯽︙ الزر مُفعّل بالفعل.**")
@zedub.zed_cmd(pattern=r"الذكاء تعطيل")
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
            response = requests.get(f'https://gptzaid.zaidbot.repl.co/1/text={text}').text
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

@zedub.zed_cmd(pattern="نشر")
async def Hussein(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    chat = event.chat_id
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await edit_delete(
            event, "⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️"
        )
    zedub = event.client
    global aljoker
    aljoker = True
    await aljoker_nshr(zedub, sleeptimet, chat, message, seconds)
@zedub.zed_cmd(pattern="ايقاف (النشر|نشر)")
async def stop_aljoker(event):
    global aljoker
    aljoker = False
    await event.edit("**᯽︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
#ها هم تريد تخمط بمحرم ؟ روح شوفلك موكب واضرب زنجيل احسن من ماتخمط
Ya_Hussein = False
active_joker = []
@zedub.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if not Ya_Hussein:
        return
    if event.is_private or event.chat_id not in active_joker:
        return
    sender_id = event.sender_id
    if sender_id != 6300938349:
        if isinstance(event.message.entities, list) and any(isinstance(entity, MessageEntityCustomEmoji) for entity in event.message.entities):
            await event.delete()
            sender = await event.get_sender()
            aljoker_entity = await zedub.get_entity(sender.id)
            aljoker_profile = f"[{aljoker_entity.first_name}](tg://user?id={aljoker_entity.id})"
            await event.reply(f"**᯽︙ عذرًا {aljoker_profile}، يُرجى عدم إرسال الرسائل التي تحتوي على إيموجي المُميز**")
@zedub.zed_cmd(pattern="المميز تفعيل")
async def disable_emoji_blocker(event):
    global Ya_Hussein
    Ya_Hussein = True
    active_joker.append(event.chat_id)
    await event.edit("**᯽︙ ✓ تم تفعيل امر منع الايموجي المُميز بنجاح**")
@zedub.zed_cmd(pattern="المميز تعطيل")
async def disable_emoji_blocker(event):
    global Ya_Hussein
    Ya_Hussein = False
    active_joker.remove(event.chat_id)
    await event.edit("**᯽︙ تم تعطيل امر منع الايموجي المُميز بنجاح ✓ **")
remove_admins_aljoker = {}
#الكود تمت كتابته من قبل مطورين الجوكر اذا الك نية تخمطه اذكر حقوق السورس @jepthon
@zedub.on(events.ChatAction)
async def Hussein(event):
    if gvarstatus("Mn3_Kick"):
        if event.user_kicked:
            user_id = event.action_message.from_id
            chat = await event.get_chat()
            if chat and user_id:
                now = datetime.now()
                if user_id in remove_admins_aljoker:
                    if (now - remove_admins_aljoker[user_id]).seconds < 60:
                        admin_info = await event.client.get_entity(user_id)
                        joker_link = f"[{admin_info.first_name}](tg://user?id={admin_info.id})"
                        await event.reply(f"**᯽︙ تم تنزيل المشرف {joker_link} بسبب قيامه بعملية تفليش فاشلة 🤣**")
                        await event.client.edit_admin(chat, user_id, change_info=False)
                    remove_admins_aljoker.pop(user_id)
                    remove_admins_aljoker[user_id] = now
                else:
                    remove_admins_aljoker[user_id] = now

@zedub.zed_cmd(pattern="منع_التفليش", require_admin=True)
async def Hussein_aljoker(event):
    addgvar("Mn3_Kick", True)
    await event.edit("**᯽︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")

@zedub.zed_cmd(pattern="سماح_التفليش", require_admin=True)
async def Hussein_aljoker(event):
    delgvar("Mn3_Kick")
    await event.edit("**᯽︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")
