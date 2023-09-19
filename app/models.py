from sqlalchemy import Boolean, Column,Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String)
    xpath = Column(String)
    value = Column(String)
    alias = Column(String)