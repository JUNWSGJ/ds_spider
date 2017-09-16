from . import Base
from sqlalchemy import Column, String, Integer, DateTime
import datetime


class DsTeam(Base):
    __tablename__ = 'ds_team'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    name_short = Column(String(45))
    url = Column(String(400))
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)

    def __init__(self):
        self.create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
