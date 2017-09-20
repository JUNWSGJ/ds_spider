from . import Base
from sqlalchemy import Column, String, Integer, DateTime
import datetime


class DsMatchEventShezheng(Base):
    __tablename__ = 'ds_match_event_shezheng'
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer)
    home_away = Column(String(45))
    team_name = Column(String(45))
    time_stamp = Column(Integer)
    v = Column(Integer)
    info = Column(String(45))
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)

    def __init__(self):
        self.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
