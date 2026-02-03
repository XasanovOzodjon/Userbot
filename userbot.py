from telethon import TelegramClient
from datetime import datetime, timedelta, timezone
# from models import PrivateMessage, session
from decouple import config
from love import setup as love_setup
from type import setup as type_setup
from snake import setup as snake_setup
from magictext import setup as magictext_setup
from magic import setup as magic_setup
from saveimg import setup as saveimg_setup
from tracker import setup as tracker_setup
api_id = config("API_ID", cast=int)
api_hash = config("API_HASH")

client = TelegramClient("session", api_id, api_hash)

love_setup(client)
type_setup(client)
snake_setup(client)
magictext_setup(client)
magic_setup(client)
tracker_setup(client)
saveimg_setup(client)
# async def save_messages():
#     one_month_ago = datetime.now(timezone.utc) - timedelta(days=30)
#     saved_count = 0

#     async for dialog in client.iter_dialogs():
#         if not dialog.is_user:
#             continue
        
#         user = dialog.entity
        
#         # Botlarni o'tkazib yuborish
#         if user.bot:
#             continue
        
#         count = 0
        
#         print(f"Tekshirilmoqda: {user.username or user.first_name or user.id}")
        
#         async for message in client.iter_messages(dialog.id):
#             if not message.date:
#                 continue
            
#             msg_date = message.date if message.date.tzinfo else message.date.replace(tzinfo=timezone.utc)
            
#             if msg_date < one_month_ago:
#                 break
            
#             if not message.text:
#                 continue
            
#             exists = session.query(PrivateMessage).filter_by(
#                 user_id=user.id,
#                 date=message.date,
#                 message=message.text
#             ).first()
            
#             if exists:
#                 continue
            
#             obj = PrivateMessage(
#                 user_id=user.id,
#                 username=user.username,
#                 message=message.text,
#                 date=message.date
#             )
#             session.add(obj)
#             count += 1
#             saved_count += 1
        
#         if count > 0:
#             session.commit()
#             print(f"  -> {count} ta xabar saqlandi")
    
#     print(f"\n✅ Jami saqlangan: {saved_count} ta xabar")

async def main():
    #await save_messages()
    print("\n🤖 Userbot ishga tushdi...")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()