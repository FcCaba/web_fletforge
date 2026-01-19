"""
Item Schemas
============
Esquemas Pydantic para validación de datos de Items.
"""
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    """Esquema base para Item."""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    price: float = Field(default=0.0, ge=0)
    is_available: bool = Field(default=True)


class ItemCreate(ItemBase):
    """Esquema para crear un Item."""
    pass


class ItemUpdate(BaseModel):
    """Esquema para actualizar un Item (todos los campos opcionales)."""
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    price: Optional[float] = Field(default=None, ge=0)
    is_available: Optional[bool] = None


class ItemRead(ItemBase):
    """Esquema para leer un Item (incluye campos de solo lectura)."""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
