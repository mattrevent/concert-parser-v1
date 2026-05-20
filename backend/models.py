from database import Base
from sqlalchemy import (Column, Integer, String, Float)

class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True, index=True)
    artist = Column(String)
    city = Column(String)
    venue = Column(String)
    event_date = Column(String)
    min_price = Column(Float)
    max_price = Column(Float)
    tickets_left = Column(Integer)
    ticket_url = Column(String)