import os
import shutil
from telethon.errors.rpcerrorlist import MediaEmptyError
from iqqhtani import rickthon
from ..core.managers import edit_or_reply
from ..helpers.google_image_download import googleimagesdownload
from ..helpers.utils import reply_id
plugin_category = "@rickthon"
@rickthon.iq_cmd(pattern="رابط الحذف")
async def _(kno):
    await edit_or_reply (kno, "**رابـط الحـذف ↬** https://telegram.org/deactivate \n\n ** بـوت الحـذف  ↬** @LC6BOT ")
