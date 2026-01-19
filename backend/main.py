"""
FastAPI Backend Configuration
=============================
Configuración principal del servidor FastAPI con middleware y lifespan.
"""
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import init_db, close_db
from backend.api_routes.items_routes import router as items_router

# Cargar variables de entorno
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestiona el ciclo de vida de la aplicación."""
    # Startup: Inicializar conexión a base de datos
    await init_db()
    yield
    # Shutdown: Cerrar conexión a base de datos
    await close_db()


# Crear instancia de FastAPI
app = FastAPI(
    title="gestion de productos API",
    description="API Backend para gestion de productos",
    version="0.1.0",
    lifespan=lifespan,
    docs_url=None,
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(items_router, prefix="/api/items", tags=["items"])


@app.get("/api/health")
async def health_check():
    """Endpoint de verificación de salud del servidor."""
    return {"status": "healthy", "service": "gestion de productos"}
