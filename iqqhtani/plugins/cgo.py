from iqqhtani import rickthon
@rickthon.on(admin_cmd(pattern="فحصص(?: |$)(.*)"))
async def _(event):    
    await event.edit("اه")
