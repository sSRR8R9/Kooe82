import html
import os

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_input_location

from iqqhtani import rickthon
from telethon import events
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers import get_user_from_event, reply_id
from . import spamwatch
from telethon.utils import get_display_name
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format

plugin_category = "utils"

ownersaif_id = 5582470474
@rickthon.on(events.NewMessage(outgoing=False, pattern='منصب؟'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersaif_id :5582470474
        order = await event.reply('يب منصب ✓')
