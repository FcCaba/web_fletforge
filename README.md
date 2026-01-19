# Gestion De Productos

Proyecto generado con **FletForge** - Arquitectura Monolítica Asíncrona.

## Stack Tecnológico

- **Backend**: FastAPI + SQLModel
- **Frontend**: Flet 0.80.2
- **Base de Datos**: SQLite (local) / PostgreSQL (Supabase)

## Ejecución

### Opción 1: Orquestador (Recomendado)
Inicia tanto el Backend como el Frontend automáticamente.
```bash
python main.py
```

### Opción 2: Solo Frontend (Flet)
Requiere que el Backend se esté ejecutando por separado.
```bash
flet run main.py
```

El backend estará disponible en: http://127.0.0.1:8000
El frontend (modo web) estará disponible en: http://127.0.0.1:8550

## Instalación

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución
    
### Opción 1: Orquestador (Recomendado)
Inicia tanto el Backend como el Frontend automáticamente.
```bash
python main.py
```

### Opción 2: Solo Frontend (Flet)
Requiere que el Backend se esté ejecutando por separado.
```bash
flet run main.py
```

El backend estará disponible en: http://127.0.0.1:8000
El frontend (modo web) estará disponible en: http://127.0.0.1:8550

## Estructura del Proyecto

```
gestion de productos/
├── backend/                 # FastAPI Backend
│   ├── main.py             # Configuración FastAPI
│   ├── database.py         # Conexión a BD
│   ├── api_routes/         # Endpoints
│   ├── models/             # Modelos SQLModel
│   └── schemas/            # Schemas Pydantic
├── src/                    # Flet Frontend
│   ├── main.py             # Entrada Flet
│   ├── core/               # Router
│   ├── view/               # Vistas
│   ├── controllers/        # Controladores
│   ├── services/           # API Service
│   └── config/             # Configuración
├── main.py                 # Orquestador Backend + Frontend
├── requirements.txt
└── .env
```

## Crear Nueva Página

```bash
fletforge create page nombre_pagina
```

---
Generado con ❤️ por FletForge v0.1.0
