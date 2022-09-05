from iqqhtani import rickthon
from ..core.managers import edit_or_reply
from ..helpers.utils import reply_id
plugin_category = "@rickthon"
@rickthon.iq_cmd(pattern="رابط الحذف")
async def _(rick):
    await edit_or_reply (rick, "**رابـط الحـذف ↬** https://telegram.org/deactivate \n\n ** بـوت الحـذف  ↬** @LC6BOT ")
