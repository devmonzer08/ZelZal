import asyncio
import random, re
from telethon import events
from Zara.utils import admin_cmd 

@borg.on(admin_cmd(pattern="همسه ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    wspr_bot = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    ton = await bot.inline_query(wspr_bot, input_str) 
    await ton[0].click(event.chat_id)
    await event.delete()
    
@borg.on(admin_cmd("الهمسه"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("**- شـرح كتابة همسـه سـرية :\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n- ارسـل الامـر  (** .همسه + الرسالة + معرف الشخص **)\n- مثـــال :**\n`.همسه هلو @devzein`")
        
