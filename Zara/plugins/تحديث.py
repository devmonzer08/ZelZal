
import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from Zara import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


@zedub.zed_cmd(
    pattern="ريست انستا ?(.*)",
    command=("ريست انستا", plugin_category),
    info={
        "header": "لـ جـلب معلـومـات عـن رقـم هـاتف معيـن .. الأمـر يدعـم الـدول التـاليـة ↵ 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 .. سيـتم اضـافـة بقيـة الـدول العـربيـة قريبـاً",
        "الأستـخـدام": "{tr}كاشف + اسـم الدولـة + الـرقـم بـدون مفتـاح الـدولة",
    },
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . كـاشف الأࢪقـام الـ؏ـࢪبيـة 📲.. أࢪسـل** `.الكاشف` **للتعليـمات 𓅫╰**"
        )
    chat = "@e1_r_bot"
    zzzzl1l = await edit_or_reply(event, "**╮•⎚ جـارِ عمل ريست للاميل  📲 ⌭ . . .**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6163601803)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit("**╮•⎚ تحـقق من أنـك لم تقـم بحظر البوت @e1_r_bot .. ثم اعـد استخدام الأمـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzzzl1l.edit("**عـذرًا مـطـوري لم أقـدر على مـعرفة نـوع الـرقـم**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(
    pattern="اسبام اميل ?(.*)",
    command=("اسبام ايميل", plugin_category),
    info={
        "header": "لـ جـلب معلـومـات عـن رقـم هـاتف معيـن .. الأمـر يدعـم الـدول التـاليـة ↵ 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 .. سيـتم اضـافـة بقيـة الـدول العـربيـة قريبـاً",
        "الأستـخـدام": "{tr}كاشف + اسـم الدولـة + الـرقـم بـدون مفتـاح الـدولة",
    },
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . كـاشف الأࢪقـام الـ؏ـࢪبيـة 📲.. أࢪسـل** `.الكاشف` **للتعليـمات 𓅫╰**"
        )
    chat = "@ ip_info_rafdynywn_bot"
    zzzzl1l = await edit_or_reply(event, "**╮•⎚ جـارِ عمل اسبام ن الاميل  📲 ⌭ . . .**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6060132745)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit("**╮•⎚ تحـقق من أنـك لم تقـم بحظر البوت @ ip_info_rafdynywn_bot .. ثم اعـد استخدام الأمـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzzzl1l.edit("**عـذرًا مـطـوري لم أقـدر على مـعرفة نـوع الـرقـم**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(
    pattern="الايبي ?(.*)",
    command=("الايبي", plugin_category),
    info={
        "header": "لـ جـلب معلـومـات عـن رقـم هـاتف معيـن .. الأمـر يدعـم الـدول التـاليـة ↵ 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 .. سيـتم اضـافـة بقيـة الـدول العـربيـة قريبـاً",
        "الأستـخـدام": "{tr}كاشف + اسـم الدولـة + الـرقـم بـدون مفتـاح الـدولة",
    },
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . كـاشف الأࢪقـام الـ؏ـࢪبيـة 📲.. أࢪسـل** `.الكاشف` **للتعليـمات 𓅫╰**"
        )
    chat = "@ip_info_rafdynywn_bot"
    zzzzl1l = await edit_or_reply(event, "**╮•⎚ جـارِ الكشف عن الايبي  📲 ⌭ . . .**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6067541039)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit("**╮•⎚ تحـقق من أنـك لم تقـم بحظر البوت @ ip_info_rafdynywn_bot .. ثم اعـد استخدام الأمـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzzzl1l.edit("**عـذرًا مـطـوري لم أقـدر على مـعرفة نـوع الـرقـم**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(
    pattern="رشق ?(.*)",
    command=("رشق", plugin_category),
    info={
        "header": "لـ جـلب معلـومـات عـن رقـم هـاتف معيـن .. الأمـر يدعـم الـدول التـاليـة ↵ 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 .. سيـتم اضـافـة بقيـة الـدول العـربيـة قريبـاً",
        "الأستـخـدام": "{tr}كاشف + اسـم الدولـة + الـرقـم بـدون مفتـاح الـدولة",
    },
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . كـاشف الأࢪقـام الـ؏ـࢪبيـة 📲.. أࢪسـل** `.الكاشف` **للتعليـمات 𓅫╰**"
        )
    chat = "@Sezarrshq2bot"
    zzzzl1l = await edit_or_reply(event, "**╮•⎚ جـارِ رشق البوست  📲 ⌭ . . .**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6552893196)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit("**╮•⎚ تحـقق من أنـك لم تقـم بحظر البوت @Sezarrshq2bot .. ثم اعـد استخدام الأمـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzzzl1l.edit("**عـذرًا مـطـوري لم أقـدر على مـعرفة نـوع الـرقـم**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)
            
            
@zedub.zed_cmd(
    pattern="كاشف ?(.*)",
    command=("كاشف", plugin_category),
    info={
        "header": "لـ جـلب معلـومـات عـن رقـم هـاتف معيـن .. الأمـر يدعـم الـدول التـاليـة ↵ 🇾🇪🇸🇦🇦🇪🇰🇼🇶🇦🇧🇭🇴🇲 .. سيـتم اضـافـة بقيـة الـدول العـربيـة قريبـاً",
        "الأستـخـدام": "{tr}كاشف + اسـم الدولـة + الـرقـم بـدون مفتـاح الـدولة",
    },
)
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**╮ . كـاشف الأࢪقـام الـ؏ـࢪبيـة 📲.. أࢪسـل** `.الكاشف` **للتعليـمات 𓅫╰**"
        )
    chat = "@alhber192_bot"
    zzzzl1l = await edit_or_reply(event, "**╮•⎚ جـارِ الكشف عن الرقم  📲 ⌭ . . .**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=5808058772)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzzzl1l.edit("**╮•⎚ تحـقق من أنـك لم تقـم بحظر البوت @alhber192_bot .. ثم اعـد استخدام الأمـر ...🤖♥️**")
            return
        if response.text.startswith("I can't find that"):
            await zzzzl1l.edit("**عـذرًا مـطـوري لم أقـدر على مـعرفة نـوع الـرقـم**")
        else:
            await zzzzl1l.delete()
            await event.client.send_message(event.chat_id, response.message)            