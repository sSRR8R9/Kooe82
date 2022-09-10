import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from iqqhtani.utils import admin_cmd

@borg.on(admin_cmd("سبوتيفاي ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("` ضع رابط ثم حاول مره اخرى`**(._.)**")
    else:
        await event.edit("🎶**جاري التنزيل!**🎶")
    bot = "@DeezLoadBot"
    
    async with borg.conversation("@DeezLoadBot") as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              try:
                  await borg(ImportChatInviteRequest('AAAAAFZPuYvdW1A8mrT8Pg'))
              except UserAlreadyParticipantError:
                  await asyncio.sleep(0.00000069420)
              await conv.send_message(d_link)
              details = await conv.get_response()
              await borg.send_message(event.chat_id, details)
              await conv.get_response()
              songh = await conv.get_response()
              await borg.send_file(event.chat_id, songh, caption="🔆**الاغنـية المحـمـلة!**🔆")
              await event.delete()
          except YouBlockedUserError:
              await event.edit("**Error:** `فك الحظر عن` @DeezLoadBot `ثم حاول!`")