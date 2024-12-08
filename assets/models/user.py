# assets/models/user.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Relationships
    department = relationship('Department', back_populates='users')
    assets = relationship('Asset', back_populates='user')
