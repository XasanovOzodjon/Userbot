import asyncio
from telethon import events

def setup(client):

    @client.on(events.NewMessage(pattern=r"!ok", outgoing=True))
    async def save_image_handler(event):
        reply = await event.get_reply_message()
        
        await event.delete()
        
        if not reply or not reply.media:
            return
        
        try:
            me = await client.get_me()
            await client.forward_messages(me.id, reply)
        except:
            try:
                file = await reply.download_media()
                await client.send_file(me.id, file)
                
                import os
                if file and os.path.exists(file):
                    os.remove(file)
            except:
                pass