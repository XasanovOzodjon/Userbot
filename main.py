from telethon import TelegramClient
from datetime import datetime, timedelta, timezone
from models import PrivateMessage, session
from decouple import config

api_id = config("API_ID", cast=int)
api_hash = config("API_HASH")

client = TelegramClient("session", api_id, api_hash)

async def main():
    one_month_ago = datetime.now(timezone.utc) - timedelta(days=30)
    
    saved_count = 0
    
    async for dialog in client.iter_dialogs():
        if not dialog.is_user:
            continue
        
        user = dialog.entity
        count = 0
        
        print(f"Tekshirilmoqda: {user.username or user.first_name or user.id}")
        
        async for message in client.iter_messages(dialog.id):
            if not message.date:
                continue
            
            msg_date = message.date if message.date.tzinfo else message.date.replace(tzinfo=timezone.utc)
            
            if msg_date < one_month_ago:
                break
            
            if not message.text:
                continue
            
            # Duplicate tekshirish
            exists = session.query(PrivateMessage).filter_by(
                user_id=user.id,
                date=message.date,
                message=message.text
            ).first()
            
            if exists:
                continue
            
            obj = PrivateMessage(
                user_id=user.id,
                username=user.username,
                message=message.text,
                date=message.date
            )
            session.add(obj)
            count += 1
            saved_count += 1
        
        if count > 0:
            session.commit()
            print(f"  -> {count} ta xabar saqlandi")
    
    print(f"\n✅ Jami saqlangan: {saved_count} ta xabar")

with client:
    client.loop.run_until_complete(main())