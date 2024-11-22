from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Logs(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    image_name = Column(String)
    timestamp = Column(DateTime)

    def __init__(self, user_name, image_name, timestamp):
        self.user_name = user_name
        self.image_name = image_name
        self.timestamp = timestamp
