from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime


# Defining db table as Python class

class ShortURL(Base):
    __tablename__ = "short_urls"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    short_code = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    access_count = Column(Integer, default=0)
