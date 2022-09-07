@rickthon.on(events.NewMessage(outgoing=True, pattern=r".تيك توك"))
async def i(event):
    ac = open("accx.txt","r")
    acc = ac.readlines()[random.randint(1,366)]
    await rickthon.send_message(event.chat_id,f"• لديك حسابك الان ..\n• {acc}")