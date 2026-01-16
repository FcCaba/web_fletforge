# FletForge 🚀 - Guía Completa del Proyecto

Este proyecto utiliza **FletForge**, una arquitectura profesional para Flet que automatiza el MVC, servicios, componentes y temas dinámicos.

---

## 🏗️ Arquitectura del Proyecto

Tu proyecto está organizado siguiendo principios de diseño modular:

-   **`src/services/`**: Lógica de negocio, APIs y persistencia de datos.
-   **`src/config/`**: Configuración global (`settings.py`) e identidad visual (`theme.py`).
-   **`src/view/layout/`**: Estructuras base de la interfaz (AppBar, Footers, etc.).
-   **`src/view/components/`**: Piezas visuales pequeñas y reutilizables.
-   **`src/view/page/`**: Vistas completas de la aplicación.
-   **`src/controllers/`**: Manejadores de eventos (Lógica de la UI).
-   **`src/models/`**: Estado y estructuras de datos.

---

## 🎨 Identidad Visual y Temas (`src/config/theme.py`)

Ahora puedes cambiar el look de toda tu aplicación desde un solo lugar:
- Edita los colores en `theme.py` para actualizar `PRIMARY`, `SURFACE`, `BACKGROUND`, etc.
- Todas las páginas y componentes heredarán estos colores automáticamente.

---

## 🛠️ Comandos de la CLI de FletForge

### 1. Creación de Componentes
Automatiza la generación de archivos con su estructura base:
- `fletforge create page <Nombre> -r`  -> Crea Page, Controller y Model (con ruta).
- `fletforge create service <Nombre>` -> Crea un servicio en la capa de lógica.
- `fletforge create component <Nombre>` -> Crea un componente visual reutilizable.

### 2. Ejecución y Desarrollo
- `fletforge run` -> Inicia la aplicación (detecta plataforma automáticamente).
- `fletforge run test` -> Ejecuta los tests unitarios en `tests/unit`.

---

## 🌍 Internacionalización (i18n)
Usa el sistema de traducciones tipado en `src/i18n/`:
1. Define tus textos en `es.py` o `en.py`.
2. Accede con `from i18n.manager import i18n`.
3. Usa el autocompletado: `i18n.tu_variable`.

---

## ⚙️ Configuración (`src/config/settings.py`)
- **`PLATFORM`**: "web", "desktop" o "mobile".
- **`THEME_MODE`**: "light" o "dark".
- **`FONTS`**: Registro de fuentes locales en `assets/fonts/`.

Desarrollado con ❤️ para crear apps Flet increíbles. 🔥🚀💎
