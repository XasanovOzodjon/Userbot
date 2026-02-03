from sqlalchemy import create_engine, Column, Integer, BigInteger, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://ozod:anime@localhost:5432/telegram_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base = declarative_base()

class PrivateMessage(Base):
    __tablename__ = "private_messages"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    username = Column(Text)
    message = Column(Text)
    date = Column(DateTime)

Base.metadata.create_all(engine)
