import flet as ft
import json
import os

class PersistenceService:
    """
    Servicio de Persistencia Híbrida.
    Intenta usar Flet ClientStorage (Web/Modern).
    Si falla, usa un archivo JSON local (Desktop/Legacy).
    """
    def __init__(self, page: ft.Page):
        self.page = page
        self.file_path = "settings.json"
        self._cache = {}
        self._load_local()

    def _load_local(self):
        """Carga configuraciones del archivo local si existe."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    self._cache = json.load(f)
            except Exception as e:
                print(f"[Persistence] Error loading local file: {e}")

    def _save_local(self):
        """Guarda configuraciones en archivo local."""
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(self._cache, f)
        except Exception as e:
            print(f"[Persistence] Error saving local file: {e}")

    def set(self, key: str, value):
        """Guarda un valor (intenta ClientStorage, fallback a JSON)."""
        # 1. Intentar Flet ClientStorage
        try:
            if hasattr(self.page, 'client_storage') and self.page.client_storage:
                self.page.client_storage.set(key, value)
        except Exception:
            pass # Fallo silencioso en client_storage
            
        # 2. Siempre actualizar cache y archivo local (Robustez Desktop)
        self._cache[key] = value
        self._save_local()

    def get(self, key: str, default=None):
        """Recupera un valor (prioridad ClientStorage, luego JSON)."""
        # 1. Intentar Flet ClientStorage
        try:
            if hasattr(self.page, 'client_storage') and self.page.client_storage:
                if self.page.client_storage.contains_key(key):
                    return self.page.client_storage.get(key)
        except Exception:
            pass
            
        # 2. Fallback a Cache Local
        return self._cache.get(key, default)

    def clear(self):
        try:
            if hasattr(self.page, 'client_storage'):
                self.page.client_storage.clear()
        except: pass
        
        self._cache = {}
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
