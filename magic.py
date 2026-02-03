import asyncio
import random
from telethon import events
from telethon.errors import FloodWaitError, MessageNotModifiedError

def setup(client):

    async def safe_edit(msg, text):
        try:
            await msg.edit(text)
            return True
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
            return False
        except:
            return False

    @client.on(events.NewMessage(pattern=r"!magic2(?:\s+(.+))?$", outgoing=True))
    async def magic2_handler(event):
        await event.delete()
        
        custom_text = event.pattern_match.group(1)
        if custom_text:
            words = custom_text.split()
        else:
            words = ["MEN", "SIZNI", "SEVAMAN", "😍"]
        
        arr = ["🥰", "😚", "☺️", "😘", "🤭", "😍", "😙", "🙃", "🤗"]
        h = "◽"
        r = "🥰"
        
        msg = await event.respond(h)
        
        # 1-qism: Yurak chiziladi
        heart_lines = [
            h*9,
            h*2 + arr[0]*2 + h + arr[0]*2 + h*2,
            h + arr[0]*7 + h,
            h + arr[0]*7 + h,
            h + arr[0]*7 + h,
            h*2 + arr[0]*5 + h*2,
            h*3 + arr[0]*3 + h*3,
            h*4 + arr[0] + h*4,
        ]
        
        first = ""
        for line in heart_lines:
            first += line + "\n"
            await safe_edit(msg, first)
            await asyncio.sleep(0.15)
        
        # 2-qism: Emoji almashadi
        for i in arr:
            heart = "\n".join([
                h*9,
                h*2 + i*2 + h + i*2 + h*2,
                h + i*7 + h,
                h + i*7 + h,
                h + i*7 + h,
                h*2 + i*5 + h*2,
                h*3 + i*3 + h*3,
                h*4 + i + h*4,
                h*9
            ])
            await safe_edit(msg, heart)
            await asyncio.sleep(0.25)
        
        # 3-qism: Tasodifiy emojilar
        for _ in range(5):
            rand = random.choices(arr, k=34)
            random_heart = "\n".join([
                h*9,
                h*2 + rand[0] + rand[1] + h + rand[2] + rand[3] + h*2,
                h + rand[4] + rand[5] + rand[6] + rand[7] + rand[8] + rand[9] + rand[10] + h,
                h + rand[11] + rand[12] + rand[13] + rand[14] + rand[15] + rand[16] + rand[17] + h,
                h + rand[18] + rand[19] + rand[20] + rand[21] + rand[22] + rand[23] + rand[24] + h,
                h*2 + rand[25] + rand[26] + rand[27] + rand[28] + rand[29] + h*2,
                h*3 + rand[30] + rand[31] + rand[32] + h*3,
                h*4 + rand[33] + h*4,
                h*9
            ])
            await safe_edit(msg, random_heart)
            await asyncio.sleep(0.25)
        
        # 4-qism: Oq rangdan emojiga
        frames = [
            r*9 + "\n" + h*2 + arr[0]*2 + h + arr[0]*2 + h*2 + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + h + arr[0]*7 + h + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r*2 + arr[0]*5 + r*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r*2 + arr[0]*5 + r*2 + "\n" + r*3 + arr[0]*3 + r*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r*2 + arr[0]*5 + r*2 + "\n" + r*3 + arr[0]*3 + r*3 + "\n" + r*4 + arr[0] + r*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r*2 + arr[0]*5 + r*2 + "\n" + r*3 + arr[0]*3 + r*3 + "\n" + r*4 + arr[0] + r*4 + "\n" + r*9,
        ]
        
        for frame in frames:
            await safe_edit(msg, frame)
            await asyncio.sleep(0.2)
        
        # 5-qism: Yurak kichrayadi
        for i in range(8, 0, -1):
            small = (arr[0] * i + "\n") * i
            await safe_edit(msg, small)
            await asyncio.sleep(0.25)
        
        # 6-qism: Xabar so'zma-so'z
        current_text = ""
        for word in words:
            if current_text:
                current_text += " " + word
            else:
                current_text = word
            await safe_edit(msg, f"**{current_text}**")
            await asyncio.sleep(0.4)

    @client.on(events.NewMessage(pattern=r"!magic(?:\s+(.+))?$", outgoing=True))
    async def magic_handler(event):
        # !magic2 ni o'tkazib yuborish
        if event.text.startswith("!magic2"):
            return
            
        await event.delete()
        
        custom_text = event.pattern_match.group(1)
        if custom_text:
            words = custom_text.split()
        else:
            words = ["MEN", "SIZNI", "SEVAMAN", "❤️"]
        
        arr = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "💖"]
        h = "🤍"
        r = "❤️"
        
        msg = await event.respond(h)
        
        # 1-qism: Yurak chiziladi
        heart_lines = [
            h*9,
            h*2 + arr[0]*2 + h + arr[0]*2 + h*2,
            h + arr[0]*7 + h,
            h + arr[0]*7 + h,
            h + arr[0]*7 + h,
            h*2 + arr[0]*5 + h*2,
            h*3 + arr[0]*3 + h*3,
            h*4 + arr[0] + h*4,
        ]
        
        first = ""
        for line in heart_lines:
            first += line + "\n"
            await safe_edit(msg, first)
            await asyncio.sleep(0.15)
        
        # 2-qism: Ranglar almashadi
        for i in arr:
            heart = "\n".join([
                h*9,
                h*2 + i*2 + h + i*2 + h*2,
                h + i*7 + h,
                h + i*7 + h,
                h + i*7 + h,
                h*2 + i*5 + h*2,
                h*3 + i*3 + h*3,
                h*4 + i + h*4,
                h*9
            ])
            await safe_edit(msg, heart)
            await asyncio.sleep(0.25)
        
        # 3-qism: Tasodifiy ranglar
        for _ in range(5):
            rand = random.choices(arr, k=34)
            random_heart = "\n".join([
                h*9,
                h*2 + rand[0] + rand[1] + h + rand[2] + rand[3] + h*2,
                h + rand[4] + rand[5] + rand[6] + rand[7] + rand[8] + rand[9] + rand[10] + h,
                h + rand[11] + rand[12] + rand[13] + rand[14] + rand[15] + rand[16] + rand[17] + h,
                h + rand[18] + rand[19] + rand[20] + rand[21] + rand[22] + rand[23] + rand[24] + h,
                h*2 + rand[25] + rand[26] + rand[27] + rand[28] + rand[29] + h*2,
                h*3 + rand[30] + rand[31] + rand[32] + h*3,
                h*4 + rand[33] + h*4,
                h*9
            ])
            await safe_edit(msg, random_heart)
            await asyncio.sleep(0.25)
        
        # 4-qism: Oq rangdan qizilga
        frames = [
            r*9 + "\n" + h*2 + arr[0]*2 + h + arr[0]*2 + h*2 + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + h + arr[0]*7 + h + "\n" + h + arr[0]*7 + h + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + h + arr[0]*7 + h + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + h*2 + arr[0]*5 + h*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r*2 + arr[0]*5 + r*2 + "\n" + h*3 + arr[0]*3 + h*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r*2 + arr[0]*5 + r*2 + "\n" + r*3 + arr[0]*3 + r*3 + "\n" + h*4 + arr[0] + h*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r*2 + arr[0]*5 + r*2 + "\n" + r*3 + arr[0]*3 + r*3 + "\n" + r*4 + arr[0] + r*4 + "\n" + h*9,
            r*9 + "\n" + r*2 + arr[0]*2 + r + arr[0]*2 + r*2 + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r + arr[0]*7 + r + "\n" + r*2 + arr[0]*5 + r*2 + "\n" + r*3 + arr[0]*3 + r*3 + "\n" + r*4 + arr[0] + r*4 + "\n" + r*9,
        ]
        
        for frame in frames:
            await safe_edit(msg, frame)
            await asyncio.sleep(0.2)
        
        # 5-qism: Yurak kichrayadi
        for i in range(8, 0, -1):
            small = (arr[0] * i + "\n") * i
            await safe_edit(msg, small)
            await asyncio.sleep(0.25)
        
        # 6-qism: Xabar so'zma-so'z
        current_text = ""
        for word in words:
            if current_text:
                current_text += " " + word
            else:
                current_text = word
            await safe_edit(msg, f"**{current_text}**")
            await asyncio.sleep(0.4)