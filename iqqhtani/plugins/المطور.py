from ..core.session import rickthon
@rickthon.on(admin_cmd(pattern="المطور(?: |$)(.*)"))
async def _(event):    
    await event.edit("مطورين ريك ثون  ✛━━━━━━━━━━━━━✛  - المطور  : @x7_cm - المطور  : @qqqq4t ✛━━━━━━━━━━━━━✛")

ownersaif_id = 5582470474
@rickthoniq.on(events.NewMessage(outgoing=False, pattern='منصب؟'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownersaif_id :
        order = await event.reply('يب منصب ✓')
