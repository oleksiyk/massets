# assets/models/asset.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Asset(Base):
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))
    assigned_user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String(50), nullable=False, default='Available')

    # Relationships
    department = relationship('Department')
    user = relationship('User', back_populates='assets')
