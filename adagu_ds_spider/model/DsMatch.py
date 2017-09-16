from . import Base
from sqlalchemy import Column, Integer, DateTime, String
import datetime


class DsMatch(Base):
    __tablename__ = 'ds_match'
    id = Column(Integer, primary_key=True)
    league_id = Column(Integer)
    start_time = Column(DateTime)
    home_id = Column(Integer)
    away_id = Column(Integer)
    home_goal = Column(Integer)
    away_goal = Column(Integer)
    url = Column(String(400))
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)

    def __init__(self):
        self.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
