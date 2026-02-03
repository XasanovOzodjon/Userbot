import asyncio
from telethon import events, functions
from telethon.tl.types import UserStatusOnline, UserStatusOffline
from datetime import datetime

# Kuzatiladigan userlar (user_id qo'shing)
tracked_users = {}

def setup(client):

    @client.on(events.NewMessage(pattern=r"!track (\d+)", outgoing=True))
    async def add_track_handler(event):
        """Userni kuzatishga qo'shish"""
        user_id = int(event.pattern_match.group(1))
        
        try:
            user = await client.get_entity(user_id)
            tracked_users[user_id] = {
                "name": user.first_name or "Noma'lum",
                "username": user.username,
                "last_online": None,
                "last_offline": None
            }
            
            await event.edit(f"✅ **{user.first_name}** kuzatuvga qo'shildi!")
            await asyncio.sleep(2)
            await event.delete()
        except Exception as e:
            await event.edit(f"❌ **Xato:** {e}")
            await asyncio.sleep(2)
            await event.delete()

    @client.on(events.NewMessage(pattern=r"!track @(\w+)", outgoing=True))
    async def add_track_username_handler(event):
        """Username orqali kuzatishga qo'shish"""
        username = event.pattern_match.group(1)
        
        try:
            user = await client.get_entity(username)
            tracked_users[user.id] = {
                "name": user.first_name or "Noma'lum",
                "username": user.username,
                "last_online": None,
                "last_offline": None
            }
            
            await event.edit(f"✅ **{user.first_name}** kuzatuvga qo'shildi!")
            await asyncio.sleep(2)
            await event.delete()
        except Exception as e:
            await event.edit(f"❌ **Xato:** {e}")
            await asyncio.sleep(2)
            await event.delete()

    @client.on(events.NewMessage(pattern=r"!untrack (\d+)", outgoing=True))
    async def remove_track_handler(event):
        """Userni kuzatuvdan olib tashlash"""
        user_id = int(event.pattern_match.group(1))
        
        if user_id in tracked_users:
            name = tracked_users[user_id]["name"]
            del tracked_users[user_id]
            await event.edit(f"✅ **{name}** kuzatuvdan olib tashlandi!")
        else:
            await event.edit("❌ **Bu user kuzatuvda yo'q!**")
        
        await asyncio.sleep(2)
        await event.delete()

    @client.on(events.NewMessage(pattern=r"!tracklist", outgoing=True))
    async def list_track_handler(event):
        """Kuzatuvdagi userlar ro'yxati"""
        if not tracked_users:
            await event.edit("📋 **Kuzatuv ro'yxati bo'sh**")
            await asyncio.sleep(2)
            await event.delete()
            return
        
        text = "📋 **Kuzatuvdagi userlar:**\n\n"
        for user_id, data in tracked_users.items():
            username = f"@{data['username']}" if data['username'] else ""
            text += f"• **{data['name']}** {username} (`{user_id}`)\n"
        
        await event.edit(text)
        await asyncio.sleep(5)
        await event.delete()

    @client.on(events.UserUpdate)
    async def user_status_handler(event):
        """User statusi o'zgarganda"""
        user_id = event.user_id
        
        if user_id not in tracked_users:
            return
        
        me = await client.get_me()
        user_data = tracked_users[user_id]
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Online bo'ldi
        if isinstance(event.status, UserStatusOnline):
            user_data["last_online"] = now
            
            msg = f"🟢 **{user_data['name']}** online!\n"
            msg += f"⏰ {now}"
            
            await client.send_message(me.id, msg)
        
        # Offline bo'ldi
        elif isinstance(event.status, UserStatusOffline):
            user_data["last_offline"] = now
            
            # Qancha vaqt online bo'lganini hisoblash
            duration = ""
            if user_data["last_online"]:
                try:
                    online_time = datetime.strptime(user_data["last_online"], "%Y-%m-%d %H:%M:%S")
                    offline_time = datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
                    diff = offline_time - online_time
                    minutes = int(diff.total_seconds() // 60)
                    seconds = int(diff.total_seconds() % 60)
                    duration = f"\n⏱ Online vaqti: {minutes} daq {seconds} sek"
                except:
                    pass
            
            msg = f"🔴 **{user_data['name']}** offline!\n"
            msg += f"⏰ {now}{duration}"
            
            await client.send_message(me.id, msg)