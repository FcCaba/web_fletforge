"""
API Service
===========
Servicio para comunicación asíncrona con el backend API usando httpx.
"""
import os
from typing import List, Optional, Dict, Any

import httpx
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la API
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000/api")


class ApiService:
    """Servicio para comunicación con la API backend."""
    
    def __init__(self, base_url: str = API_BASE_URL):
        """Inicializa el servicio con la URL base de la API."""
        self.base_url = base_url
        self.timeout = httpx.Timeout(30.0)
    
    async def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Realiza una petición HTTP asíncrona."""
        url = f"{self.base_url}{endpoint}"
        print(f"⚡ [API] Request: {method} {url}")
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.request(
                    method=method,
                    url=url,
                    json=data,
                    params=params
                )
                print(f"⚡ [API] Response: {response.status_code}")
                response.raise_for_status()
                
                if response.status_code == 204:
                    return None
                return response.json()
        except httpx.RequestError as e:
            print(f"❌ [API Error] Error de conexión: {e}")
            return []
        except httpx.HTTPStatusError as e:
            print(f"❌ [API Error] Error HTTP {e.response.status_code}: {e}")
            return []
        except Exception as e:
            print(f"❌ [API Error] Inesperado: {e}")
            return []
    
    # ==================== Items ====================
    
    async def get_items(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """Obtiene la lista de items."""
        return await self._request(
            "GET",
            "/items/",
            params={"skip": skip, "limit": limit}
        )
    
    async def get_item(self, item_id: int) -> Dict[str, Any]:
        """Obtiene un item por su ID."""
        return await self._request("GET", f"/items/{item_id}")
    
    async def create_item(self, item_data: Dict[str, Any]) -> Dict[str, Any]:
        """Crea un nuevo item."""
        return await self._request("POST", "/items/", data=item_data)
    
    async def update_item(self, item_id: int, item_data: Dict[str, Any]) -> Dict[str, Any]:
        """Actualiza un item existente."""
        return await self._request("PUT", f"/items/{item_id}", data=item_data)
    
    async def delete_item(self, item_id: int) -> None:
        """Elimina un item."""
        await self._request("DELETE", f"/items/{item_id}")
    
    # ==================== Health ====================
    
    async def health_check(self) -> Dict[str, Any]:
        """Verifica el estado del servidor."""
        return await self._request("GET", "/health")
