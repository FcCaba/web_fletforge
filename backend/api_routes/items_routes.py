"""
Items API Routes
================
Endpoints CRUD para el recurso Items.
"""
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from backend.database import get_session
from backend.models.item_model import Item
from backend.schemas.item_schema import ItemCreate, ItemRead, ItemUpdate

router = APIRouter()


@router.get("/", response_model=List[ItemRead])
async def get_items(
    skip: int = 0,
    limit: int = 100,
    session: AsyncSession = Depends(get_session)
):
    """Obtiene lista de items con paginación."""
    result = await session.execute(
        select(Item).offset(skip).limit(limit)
    )
    items = result.scalars().all()
    return items


@router.get("/{item_id}", response_model=ItemRead)
async def get_item(
    item_id: int,
    session: AsyncSession = Depends(get_session)
):
    """Obtiene un item por su ID."""
    result = await session.execute(
        select(Item).where(Item.id == item_id)
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item con id {item_id} no encontrado"
        )
    return item


@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(
    item_data: ItemCreate,
    session: AsyncSession = Depends(get_session)
):
    """Crea un nuevo item."""
    item = Item(**item_data.model_dump())
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


@router.put("/{item_id}", response_model=ItemRead)
async def update_item(
    item_id: int,
    item_data: ItemUpdate,
    session: AsyncSession = Depends(get_session)
):
    """Actualiza un item existente."""
    result = await session.execute(
        select(Item).where(Item.id == item_id)
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item con id {item_id} no encontrado"
        )
    
    update_data = item_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(item, key, value)
    
    await session.commit()
    await session.refresh(item)
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    item_id: int,
    session: AsyncSession = Depends(get_session)
):
    """Elimina un item."""
    result = await session.execute(
        select(Item).where(Item.id == item_id)
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item con id {item_id} no encontrado"
        )
    
    await session.delete(item)
    await session.commit()
    return None
