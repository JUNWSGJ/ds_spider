from . import Base
from sqlalchemy import Column, String, Integer, DateTime
import datetime


class DsMatchEvent(Base):
    __tablename__ = 'ds_match_event'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer)
    type = Column(String(45))
    home_away = Column(String(45))
    team_id = Column(Integer)
    team_name = Column(String(200))
    timestamp = Column(Integer)
    v = Column(Integer)
    info = Column(String(45))
    created_time = Column(DateTime, nullable=False)
    updated_time = Column(DateTime, nullable=False)

    def __init__(self):
        self.created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
