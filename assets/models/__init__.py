# assets/models/__init__.py

from .base import Base
from .department import Department
from .user import User
from .asset import Asset
from .asset_movement import AssetMovement

__all__ = ["Base", "Department", "User", "Asset", "AssetMovement"]

