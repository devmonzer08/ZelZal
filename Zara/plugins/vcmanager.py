#الملف تابع لـ سورس زدثــون
from telethon import functions
from telethon.errors import ChatAdminRequiredError, UserAlreadyInvitedError
from telethon.tl.types import Channel, Chat, User
from Zara import zedub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import mentionuser

plugin_category = "البوت"


async def get_group_call(chat):
    if isinstance(chat, Channel):
        result = await zedub(functions.channels.GetFullChannelRequest(channel=chat))
    elif isinstance(chat, Chat):
        result = await zedub(functions.messages.GetFullChatRequest(chat_id=chat.id))
    return result.full_chat.call


async def chat_vc_checker(event, chat, edits=True):
    if isinstance(chat, User):
        await edit_delete(event, "**- المحـادثـه الصـوتيـه غيـر مدعومـه هنـا ؟!**")
        return None
    result = await get_group_call(chat)
    if not result:
        if edits:
            await edit_delete(event, "**- لاتوجـد محـادثـه صوتيـه هنـا ؟!**")
        return None
    return result


async def parse_entity(entity):
    if entity.isnumeric():
        entity = int(entity)
    return await zedub.get_entity(entity)


@zedub.zed_cmd(
    pattern="بدء",
    command=("بدء", plugin_category),
    info={
        "header": "لـ بـدء المحادثـه الصـوتيـه",
        "الاستخـدام": "{tr}بدء",
    },
)
async def start_vc(event):
    "لـ بـدء المحادثـه الصـوتيـه"
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat, False)
    if gc_call:
        return await edit_delete(event, "**- المحادثـه الصوتيـه تم بـدئهـا مسبقـاً هنـا **")
    try:
        await zedub(
            functions.phone.CreateGroupCallRequest(
                peer=vc_chat,
                title="سـٰٖـ๋͜ــوُࢪس سـٰٖـ๋͜ــيزًࢪ❤️‍🩹",
            )
        )
        await edit_delete(event, "**- جـارِ بـدء محـادثـه صـوتيـه ...**")
    except ChatAdminRequiredError:
        await edit_delete(event, "**- انت بحاجـه الى صلاحيـات المشـرف لبـدء محادثـه صوتيـه ...**", time=20)


@zedub.zed_cmd(
    pattern="انهاء",
    command=("انهاء", plugin_category),
    info={
        "header": "لـ انهـاء المحادثـه الصـوتيـه",
        "الاستخـدام": "{tr}انهاء",
    },
)
async def end_vc(event):
    "لـ انهـاء المحادثـه الصـوتيـه"
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    try:
        await zedub(functions.phone.DiscardGroupCallRequest(call=gc_call))
        await edit_delete(event, "**- تم انهـاء المحـادثـه الصـوتيـه .. بنجـاح ✓**")
    except ChatAdminRequiredError:
        await edit_delete(event, "**- انت بحاجـه الى صلاحيـات المشـرف لـ انهـاء المحادثـه الصوتيـه ...**", time=20)


@zedub.zed_cmd(
    pattern="دعوه ?(.*)?",
    command=("دعوه", plugin_category),
    info={
        "header": "لـ دعـوة اشخـاص للمكالمـه",
        "الاستخـدام": "{tr}دعوه + معـرف/ايـدي الشخـص او بالـرد ع الشخـص",
        "مثــال :": [
            "{tr}دعوه @angelpro",
            "{tr}دعوه + ايـدي الشخـص الاول + ايـدي الشخص الثانـي ... الـخ",
        ],
    },
)
async def inv_vc(event):
    "لـ دعـوة اشخـاص للمكالمـه"
    users = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    if not users:
        if not reply:
            return await edit_delete("Whom Should i invite")
        users = reply.from_id
    await edit_or_reply(event, "**- جـارِ دعـوة الاشخـاص الى المكالمـه ...**")
    entities = str(users).split(" ")
    user_list = []
    for entity in entities:
        cc = await parse_entity(entity)
        if isinstance(cc, User):
            user_list.append(cc)
    try:
        await zedub(
            functions.phone.InviteToGroupCallRequest(call=gc_call, users=user_list)
        )
        await edit_delete(event, "**- تم اضافـة الاشخـاص الى المكالمـه .. بنجـاح ✓**")
    except UserAlreadyInvitedError:
        return await edit_delete(event, "**- هـذا الشخـص منضـم مسبقـاً**", time=20)


@zedub.zed_cmd(
    pattern="معلومات المكالمه",
    command=("معلومات المكالمه", plugin_category),
    info={
        "header": "لـ جلب معلومـات المحادثـه الصـوتيـه",
        "الاستخـدام": "{tr}معلومات المكالمه",
    },
)
async def info_vc(event):
    "لـ جلب معلومـات المحادثـه الصـوتيـه"
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    await edit_or_reply(event, "**- جـارِ جلب معلومـات المحـادثه الصـوتيـه ...**")
    call_details = await zedub(
        functions.phone.GetGroupCallRequest(call=gc_call, limit=1)
    )
    grp_call = "**معلومـات المحـادثـه الصـوتيـه**\n\n"
    grp_call += f"**- الاسـم :** {call_details.call.title}\n"
    grp_call += f"**- عـدد المنضميـن :** {call_details.call.participants_count}\n\n"

    if call_details.call.participants_count > 0:
        grp_call += "**- المنضميـن :**\n"
        for user in call_details.users:
            nam = f"{user.first_name or ''} {user.last_name or ''}"
            grp_call += f"  ● {mentionuser(nam,user.id)} - `{user.id}`\n"
    await edit_or_reply(event, grp_call)


@zedub.zed_cmd(
    pattern="عنوان?(.*)?",
    command=("عنوان", plugin_category),
    info={
        "header": "لـ تغييـر عنـوان المكالمـه",
        "الاستخـدام": "{tr}عنوان + نـص",
        "مثــال :": "{tr}عنوان زدثون",
    },
)
async def title_vc(event):
    "لـ تغييـر عنـوان المكالمـه"
    title = event.pattern_match.group(1)
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    if not title:
        return await edit_delete("What should i keep as title")
    await zedub(functions.phone.EditGroupCallTitleRequest(call=gc_call, title=title))
    await edit_delete(event, f"**- تم تغييـر عنـوان المكالمـه الـى {title} .. بنجـاح ✓**")


@zedub.zed_cmd(
    pattern="اكتم ([\s\S]*)",
    command=("اكتم", plugin_category),
    info={
        "header": "لـ كتم شخص في المكالمـه",
        "الاستخـدام": [
            "{tr}اكتم + معـرف/ايـدي الشخـص او بالـرد ع الشخـص",
        ],
        "مثــال :": [
            "{tr}اكتم @angelpro",
            "{tr}اكتم + ايـدي الشخـص الاول + ايـدي الشخص الثانـي ... الـخ",
        ],
    },
)
async def mute_vc(event):
    "لـ كتم شخص في المكالمـه"
    cmd = event.pattern_match.group(1)
    users = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    check = "Unmute" if cmd else "اكتم"
    if not users:
        if not reply:
            return await edit_delete(f"Whom Should i {check}")
        users = reply.from_id
    await edit_or_reply(event, f"{check[:-1]}ing User in Group Call")
    entities = str(users).split(" ")
    user_list = []
    for entity in entities:
        cc = await parse_entity(entity)
        if isinstance(cc, User):
            user_list.append(cc)

    for user in user_list:
        await zedub(
            functions.phone.EditGroupCallParticipantRequest(
                call=gc_call,
                participant=user,
                muted=bool(not cmd),
            )
        )
    await edit_delete(event, f"{check}d users in Group Call")


@zedub.zed_cmd(
    command=("الغاء الكتم", plugin_category),
    info={
        "header": "لـ الغـاء كتـم شخـص في المكالمـه",
        "الاستخـدام": [
            "{tr}الغاء الكتم + معـرف/ايـدي الشخـص او بالـرد ع الشخـص",
        ],
        "مثــال :": [
            "{tr}الغاء الكتم @angelpro",
            "{tr}الغاء الكتم + ايـدي الشخـص الاول + ايـدي الشخص الثانـي ... الـخ",
        ],
    },
)
async def unmute_vc(event):
    "لـ الغـاء كتـم شخـص في المكالمـه"
