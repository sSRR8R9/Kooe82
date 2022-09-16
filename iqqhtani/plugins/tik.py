@rickthon.on(admin_cmd(pattern="معلومات(?: |$)(.*)"))
async def _(rickthon):
    reply_message = await rickthon.get_reply_message()
    if not reply_message:
        await edit_or_reply(rickthon, "**♛ ⦙  الرد على اليوزر.**")
        return
    if not reply_message.text:
        await edit_or_reply(rickthon, "**♛ ⦙  الرد على اليوزر.**")
        return
    chat = "@inftikpybot"
    iqevent = await edit_or_reply(rickthon, "**♛ ⦙  جاري تحميل  المعلومات**")
    async with rickthon.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True, from_users=1354606430))
            await rickthon.client.forward_messages(chat, reply_message)
            response = await response
            await rickthon.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await iqevent.edit("**♛ ⦙  فك الحظر من البوت : @inftikpybot**")
            return
        if response.text.startswith("؟"):
            await iqevent.edit("?")
        else:
            await iqevent.delete()
            await rickthon.client.send_message(rickthon.chat_id, response.message)
