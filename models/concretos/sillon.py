"""
Clase concreta Sillón.
"""
from ..categorias.asientos import Asiento

class Sillon(Asiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = "tela",
                 es_reclinable: bool = False, tiene_reposapiés: bool = False):
        
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)
        self.es_reclinable = es_reclinable
        self.tiene_reposapiés = tiene_reposapiés

    # --- PROPIEDADES (Getters) ---

    @property
    def es_reclinable(self) -> bool: 
        return self._es_reclinable

    @property
    def tiene_reposapiés(self) -> bool: 
        return self._tiene_reposapiés

    # --- VALIDACIONES (Setters) ---

    @es_reclinable.setter
    def es_reclinable(self, v: bool): 
        self._es_reclinable = v

    @tiene_reposapiés.setter
    def tiene_reposapiés(self, v: bool): 
        self._tiene_reposapiés = v

    # --- MÉTODOS DE LÓGICA ---

    def calcular_precio(self) -> float:
        precio = self.precio_base * self.calcular_factor_comodidad()
        if self.es_reclinable: precio += 100.0
        if self.tiene_reposapiés: precio += 50.0
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        rec = "reclinable" if self.es_reclinable else "fijo"
        rep = "con reposapiés" if self.tiene_reposapiés else ""
        return f"Sillón {rec} '{self.nombre}' tapizado en {self.material_tapizado} {rep}."