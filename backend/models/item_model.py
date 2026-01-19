"""
Item Model
==========
Modelo de base de datos para Items usando SQLModel.
"""
from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
    """Modelo de base de datos para Item."""
    
    __tablename__ = "items"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(default=0.0, ge=0)
    is_available: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
