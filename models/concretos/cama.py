"""
Clase concreta Cama.
"""
from ..categorias.superficies import Superficie

class Cama(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tamaño: str, incluye_colchon: bool = False, tiene_cabecera: bool = True):
        
        # Dimensiones estimadas según tamaño
        dimensiones = {
            "individual": (1.0, 1.9), "matrimonial": (1.35, 1.9),
            "queen": (1.5, 2.0), "king": (2.0, 2.0)
        }
        ancho, largo = dimensiones.get(tamaño.lower(), (1.0, 1.9))
        
        super().__init__(nombre, material, color, precio_base, ancho, largo, False)
        
        self.tamaño = tamaño
        self.incluye_colchon = incluye_colchon
        self.tiene_cabecera = tiene_cabecera

    # --- PROPIEDADES (Getters) ---

    @property
    def tamaño(self) -> str:
        return self._tamaño
    
    @property
    def incluye_colchon(self) -> bool: 
        return self._incluye_colchon
    
    @property
    def tiene_cabecera(self) -> bool: 
        return self._tiene_cabecera
    
    # --- VALIDACIONES (Setters) ---
    
    @tamaño.setter
    def tamaño(self, valor: str):
        if valor.lower() not in ["individual", "matrimonial", "queen", "king"]:
            raise ValueError("Tamaño de cama inválido.")
        self._tamaño = valor.lower()

    @incluye_colchon.setter
    def incluye_colchon(self, valor: bool): self._incluye_colchon = valor


    @tiene_cabecera.setter
    def tiene_cabecera(self, valor: bool): self._tiene_cabecera = valor

    # --- MÉTODOS DE LÓGICA ---

    def calcular_precio(self) -> float:
        precio = self.precio_base
        multiplicadores = {"individual": 1.0, "matrimonial": 1.3, "queen": 1.6, "king": 2.0}
        precio *= multiplicadores.get(self.tamaño, 1.0)
        
        if self.incluye_colchon: precio += 250.0
        if self.tiene_cabecera: precio += 80.0
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        colchon = "Incluye colchón" if self.incluye_colchon else "Sin colchón"
        cabecera = "con cabecera" if self.tiene_cabecera else "sin cabecera"
        return f"Cama {self.tamaño.capitalize()} '{self.nombre}' de {self.material}. {cabecera}. {colchon}."