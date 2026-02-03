import asyncio
import random
from telethon import events

def setup(client):

    @client.on(events.NewMessage(pattern="!type (.+)", outgoing=True))
    async def typing_handler(event):
        text = event.pattern_match.group(1)
        await event.delete()
        msg = await event.respond("▌")
        
        await asyncio.sleep(0.5)  # Boshida biroz kutish
        
        result = ""
        i = 0
        
        while i < len(text):
            char = text[i]
            result += char
            
            try:
                await msg.edit(result + "▌")
            except:
                pass  # Edit limitdan o'tsa, davom etamiz
            
            # Tasodifiy tezlik (0.2 - 0.4 soniya) - sekinroq qildim
            await asyncio.sleep(random.uniform(0.2, 0.4))
            
            # 12% ehtimol bilan xato qiladi
            if random.random() < 0.12 and len(result) > 0:
                wrong_char = random.choice("asdfghjklqwertyuiopzxcvbnm")
                result += wrong_char
                try:
                    await msg.edit(result + "▌")
                except:
                    pass
                await asyncio.sleep(0.3)
                
                result = result[:-1]
                try:
                    await msg.edit(result + "▌")
                except:
                    pass
                await asyncio.sleep(0.2)
            
            # 8% ehtimol bilan pauza
            if random.random() < 0.08:
                await asyncio.sleep(random.uniform(0.2, 0.5))
            
            i += 1
        
        await asyncio.sleep(0.3)
        await msg.edit(result)