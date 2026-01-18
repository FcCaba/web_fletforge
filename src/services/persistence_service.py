import flet as ft


class PersistenceService:
    """
    Servicio de Persistencia usando Flet Shared Preferences (Async).
    Permite almacenar datos persistentes en Web, Escritorio y Móvil de forma unificada.
    """
    def __init__(self, page: ft.Page):
        self.page = page

    async def init(self):
        """
        Inicialización opcional si se requiere cargar algo previo.
        En shared_preferences generalmente no es necesario pre-cargar todo,
        pero se mantiene por compatibilidad de estructura.
        """
        pass

    async def set(self, key: str, value):
        """Guarda un valor de forma asíncrona."""
        try:
            await self.page.shared_preferences.set(key, value)
        except Exception as e:
            print(f"[Persistence] Error setting key '{key}': {e}")

    async def get(self, key: str, default=None):
        """Recupera un valor de forma asíncrona."""
        try:
            if await self.page.shared_preferences.contains_key(key):
                return await self.page.shared_preferences.get(key)
        except Exception as e:
            print(f"[Persistence] Error getting key '{key}': {e}")
        return default

    async def contains_key(self, key: str) -> bool:
        """Verifica si existe una clave."""
        try:
            return await self.page.shared_preferences.contains_key(key)
        except Exception:
            return False

    async def get_keys(self, prefix: str) -> list[str]:
        """Obtiene todas las claves que comiencen con el prefijo."""
        try:
            return await self.page.shared_preferences.get_keys(prefix)
        except Exception:
            return []

    async def remove(self, key: str):
        """Elimina una clave."""
        try:
            await self.page.shared_preferences.remove(key)
        except Exception as e:
            print(f"[Persistence] Error removing key '{key}': {e}")

    async def clear(self):
        """
        Limpia TODO el almacenamiento del usuario para esta app.
        ¡Cuidado!
        """
        try:
            await self.page.shared_preferences.clear()
        except Exception as e:
            print(f"[Persistence] Error clearing storage: {e}")

