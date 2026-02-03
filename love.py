import asyncio
from telethon import events

running_love = {}

HEARTS = [
    "❤️",
    "🧡",
    "💛",
    "💚",
    "💙",
    "💜",
    "🖤",
    "🤍"
]

def setup(client):

    @client.on(events.NewMessage(pattern="!love", outgoing=True))
    async def love_handler(event):
        chat_id = event.chat_id

        if running_love.get(chat_id):
            return

        running_love[chat_id] = True
        
        await event.delete()  # "!love" xabarini o'chirish
        msg = await event.respond(HEARTS[0])  # yangi xabar yuborish

        i = 0
        while running_love.get(chat_id):
            await asyncio.sleep(0.3)
            i = (i + 1) % len(HEARTS)
            try:
                await msg.edit(HEARTS[i])
            except:
                break

    @client.on(events.NewMessage(outgoing=True))
    async def stop_love(event):
        chat_id = event.chat_id

        if event.text and event.text.startswith("!") and event.text != "!love":
            if running_love.get(chat_id):
                running_love[chat_id] = False