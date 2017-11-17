from . import Base
from sqlalchemy import Column,String,Integer,DateTime
import datetime

class DsLeague(Base):
    __tablename__ = 'ds_league'
    id = Column(Integer,primary_key=True)
    name = Column(String(45))
    name_short = Column(String(45))
    url = Column(String(400))
    created_time = Column(DateTime,nullable=False)
    updated_time = Column(DateTime,nullable=False)

    def __init__(self):
        self.created_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
