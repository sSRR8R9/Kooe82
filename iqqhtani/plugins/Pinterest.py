# حقوق ريك ثون يحيى

import os

import re

import requests

import asyncio

from iqqhtani import rickthon

from iqqhtani.plugins import mention

from ..core.managers import edit_or_reply

from ..helpers.utils import reply_id

from urllib import request

try:

    from pyquery import PyQuery as pq

except ModuleNotFoundError:

    os.system("pip3 install pyquery")

    from pyquery import PyQuery as pq

plugin_category = "extra"

def get_download_url(link):

    post_request = requests.post('https://www.expertsphp.com/download.php', data={'url': link})

    request_content = post_request.content

    str_request_content = str(request_content, 'utf-8')

    download_url = pq(str_request_content)('table.table-condensed')('tbody')('td')('a').attr('href')

    return download_url

@rickthon.rick_cmd(

    pattern="بنترست(?:\s|$)([\s\S]*)",

    command=("بنترست", plugin_category),

    info={

        "header": "To download pinterest posts",

        "options": "To download image and video posts from pinterest",

        "usage": [

            "{tr} بنترست <post link>",

        ],

    },

)

async def pint(event):

    "To download pinterest posts"

    A = event.pattern_match.group(1)

    B = await event.get_reply_message()

    reply_to_id = await reply_id(event)

    if A:

        MINE = get_download_url(A)

    elif B and B.message:

    	MINE = get_download_url(B.message)    
        
    else:

        return await edit_delete(event, "`الرجاء الرد على الرابط 𖤍 `")

    if A and "بنترست" not in A:

        await edit_or_reply(event, "`الرابط غير صحيح 𖤍`")

        return

    elif not A and "بنترست" not in B.message:

        await edit_or_reply(event, "`الرابط غير صحيح 𖤍`")

        return

    else:

    	pass

    await edit_or_reply(event, "`جاري التحميل...`")

    await event.delete()

    await event.client.send_file(event.chat.id, MINE, caption=f"➥ by = {mention}", reply_to=reply_to_id)

    
