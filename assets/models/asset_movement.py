# assets/models/asset_movement.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class AssetMovement(Base):
    __tablename__ = 'asset_movements'

    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('assets.id'))
    from_location = Column(String(100))
    to_location = Column(String(100))
    movement_date = Column(DateTime, default=datetime.utcnow)

    # Relationships
    asset = relationship('Asset')
