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
    pattern="vc(|un)mute ([\s\S]*)",
    command=("vcmute", plugin_category),
    info={
        "header": "To mute users on Voice Chat.",
        "description": "To mute a stream on Voice Chat",
        "usage": [
            "{tr}vcmute < userid/username or reply to user >",
        ],
        "examples": [
            "{tr}vcmute @angelpro",
            "{tr}vcmute userid1 userid2",
        ],
    },
)
async def mute_vc(event):
    "To mute users in vc."
    cmd = event.pattern_match.group(1)
    users = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    vc_chat = await zedub.get_entity(event.chat_id)
    gc_call = await chat_vc_checker(event, vc_chat)
    if not gc_call:
        return
    check = "Unmute" if cmd else "Mute"
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
                call=gc_call, participant=user, muted=not cmd
            )
        )
    await edit_delete(event, f"{check}d users in Group Call")


@zedub.zed_cmd(
    command=("vcunmute", plugin_category),
    info={
        "header": "To unmute users on Voice Chat.",
        "description": "To unmute a stream on Voice Chat",
        "usage": [
            "{tr}vcunmute < userid/username or reply to user>",
        ],
        "examples": [
            "{tr}vcunmute @angelpro",
            "{tr}vcunmute userid1 userid2",
        ],
    },
)
async def unmute_vc(event):
    "To unmute users in vc."


@zedub.zed_cmd(
    pattern="(del|get|add)vcuser(?:\s|$)([\s\S]*)",
    command=("vcuser", plugin_category),
    info={
        "header": "To add user as for vc .",
        "usage": [
            "{tr}addvcuser <username/reply/mention>",
            "{tr}getvcuser",
            "{tr}delvcuser <username/reply/mention>",
        ],
    },
)
async def add_sudo_user(event):
    "To add user to sudo."
    vcusers = {}
    vc_chats = _vcusers_list()
    cmd = event.pattern_match.group(1)

    with contextlib.suppress(AttributeError):
        vcusers = sql.get_collection("vcusers_list").json

    if cmd == "get":
        if not vc_chats:
            return await edit_delete(
                event, "__There are no vc auth users for your CatZara.__"
            )
        result = "**The list of vc auth users for your CatZara are :**\n\n"
        for chat in [*vcusers]:
            result += f"☞ **Name:** {mentionuser(vcusers[str(chat)]['chat_name'],vcusers[str(chat)]['chat_id'])}\n"
            result += f"**User Id :** `{chat}`\n"
            username = f"@{vcusers[str(chat)]['chat_username']}" or "__None__"
            result += f"**Username :** {username}\n"
            result += f"Added on {vcusers[str(chat)]['date']}\n\n"
        await edit_or_reply(event, result)

    elif cmd in ["add", "del"]:
        replied_user = event.pattern_match.group(2)
        reply = await event.get_reply_message()
        if not replied_user and reply:
            replied_user = reply.from_id
        if replied_user is None:
            return
        replied_user = await zedub.get_entity(replied_user)
        if not isinstance(replied_user, User):
            return await edit_delete(event, "`Can't fetch the user...`")
        date = str(datetime.now().strftime("%B %d, %Y"))
        userdata = {
            "chat_id": replied_user.id,
            "chat_name": get_display_name(replied_user),
            "chat_username": replied_user.username,
            "date": date,
        }
        if cmd == "add":
            if replied_user.id == event.client.uid:
                return await edit_delete(event, "__You already have the access.__.")
            elif replied_user.id in (vc_chats + _sudousers_list()):
                return await edit_delete(
                    event,
                    f"{mentionuser(get_display_name(replied_user),replied_user.id)} __already have access .__",
                )
            vcusers[str(replied_user.id)] = userdata
        elif cmd == "del":
            if str(replied_user.id) not in vcusers:
                return await edit_delete(
                    event,
                    f"{mentionuser(get_display_name(replied_user),replied_user.id)} __is not in your vc auth list__.",
                )
            del vcusers[str(replied_user.id)]

        sql.del_collection("vcusers_list")
        sql.add_collection("vcusers_list", vcusers, {})
        output = f"{mentionuser(userdata['chat_name'],userdata['chat_id'])} __is {'Added to' if cmd =='add' else 'Deleted from'} your vc auth users.__\n"
        output += "**Bot is reloading to apply the changes. Please wait for a minute**"
        msg = await edit_or_reply(event, output)
        await event.client.reload(msg)