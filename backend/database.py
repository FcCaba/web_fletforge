"""
Database Configuration
======================
Conexión a base de datos con detección automática SQLite/Supabase.
Usa SQLModel para unificar modelos ORM y esquemas Pydantic.
"""
import os
from typing import Optional

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
load_dotenv()

# Detectar configuración de base de datos
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

# Configurar motor de base de datos
if DATABASE_URL:
    # Usar URL de base de datos proporcionada (PostgreSQL, MySQL, etc.)
    if DATABASE_URL.startswith("postgresql"):
        # Convertir a formato asyncpg para soporte asíncrono
        async_url = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
    else:
        async_url = DATABASE_URL
    engine = create_async_engine(async_url, echo=False)
elif SUPABASE_URL:
    # Construir URL de PostgreSQL desde Supabase
    # Formato típico: postgresql+asyncpg://user:password@host:port/database
    engine = create_async_engine(SUPABASE_URL, echo=False)
else:
    # Usar SQLite local por defecto
    SQLITE_URL = "sqlite+aiosqlite:///./database.db"
    engine = create_async_engine(
        SQLITE_URL,
        echo=False,
        connect_args={"check_same_thread": False}
    )

# Crear sesión asíncrona
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncSession:
    """Obtiene una sesión de base de datos asíncrona."""
    async with async_session() as session:
        yield session


async def init_db() -> None:
    """Inicializa la base de datos creando todas las tablas."""
    from backend.models.item_model import Item
    from sqlmodel import select
    
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    
    # Seeding inicial si la base de datos está vacía
    async with async_session() as session:
        statement = select(Item)
        result = await session.execute(statement)
        if not result.first():
            print("🌱 Sembrando datos iniciales...")
            example_items = [
                Item(name="Laptop Gamer", description="Potente laptop para gaming y trabajo pesado", price=1200.50),
                Item(name="Mouse Inalámbrico", description="Mouse ergonómico con conexión 2.4GHz", price=25.99),
                Item(name="Monitor 27' 4K", description="Monitor IPS con resolución Ultra HD", price=350.00),
            ]
            session.add_all(example_items)
            await session.commit()
            
    print("✅ Base de datos inicializada correctamente")


async def close_db() -> None:
    """Cierra la conexión a la base de datos."""
    await engine.dispose()
    print("🔌 Conexión a base de datos cerrada")
