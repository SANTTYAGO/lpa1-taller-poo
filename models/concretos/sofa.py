"""
Clase concreta Sofa.
"""
from ..categorias.asientos import Asiento

class Sofa(Asiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, tiene_respaldo: bool = True, 
                 material_tapizado: str = "tela", es_modular: bool = False, incluye_cojines: bool = False):
        
        super().__init__(nombre, material, color, precio_base, capacidad_personas, tiene_respaldo, material_tapizado)
        self.es_modular = es_modular
        self.incluye_cojines = incluye_cojines

    # --- PROPIEDADES (Getters) ---

    @property
    def es_modular(self) -> bool: return self._es_modular

    @property
    def incluye_cojines(self) -> bool: return self._incluye_cojines

    # --- VALIDACIONES (Setters) ---

    @es_modular.setter
    def es_modular(self, v: bool): self._es_modular = v

    @incluye_cojines.setter
    def incluye_cojines(self, v: bool): self._incluye_cojines = v

    # --- MÉTODOS DE LÓGICA ---

    def calcular_precio(self) -> float:
        precio = self.precio_base * self.calcular_factor_comodidad()
        precio += (self.capacidad_personas * 80.0) # Cobro por plaza
        if self.es_modular: precio *= 1.15
        if self.incluye_cojines: precio += 40.0
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        mod = "modular" if self.es_modular else "estándar"
        return f"Sofá {mod} '{self.nombre}' de {self.capacidad_personas} plazas. Tapizado en {self.material_tapizado}."