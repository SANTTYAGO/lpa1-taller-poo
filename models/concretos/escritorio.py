"""
Clase concreta Escritorio.
"""
from ..categorias.superficies import Superficie

class Escritorio(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str = "rectangular", tiene_cajones: bool = False, 
                 num_cajones: int = 0, tiene_iluminacion: bool = False):
        
        super().__init__(nombre, material, color, precio_base, 1.2, 0.6, False)
        
        self.forma = forma
        self.tiene_cajones = tiene_cajones
        self.num_cajones = num_cajones if tiene_cajones else 0
        self.tiene_iluminacion = tiene_iluminacion

    # --- PROPIEDADES (Getters) ---

    @property
    def forma(self) -> str: 
        return self._forma

    @property
    def tiene_cajones(self) -> bool: 
        return self._tiene_cajones

    @property
    def num_cajones(self) -> int: 
        return self._num_cajones

    @property
    def tiene_iluminacion(self) -> bool: 
        return self._tiene_iluminacion

    @forma.setter
    def forma(self, valor: str): 
        self._forma = valor

    @tiene_cajones.setter
    def tiene_cajones(self, valor: bool): 
        self._tiene_cajones = valor

    @num_cajones.setter
    def num_cajones(self, valor: int): 
        self._num_cajones = max(0, valor)

    @tiene_iluminacion.setter
    def tiene_iluminacion(self, valor: bool): 
        self._tiene_iluminacion = valor

    # --- MÉTODOS DE LÓGICA ---

    def calcular_precio(self) -> float:
        precio = self.precio_base
        if self.forma.lower() == "l": precio += 150.0
        if self.tiene_cajones: precio += (self.num_cajones * 20.0)
        if self.tiene_iluminacion: precio += 85.0
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        cajones = f"con {self.num_cajones} cajones" if self.tiene_cajones else "sin cajones"
        luz = "y luz RGB/LED" if self.tiene_iluminacion else ""
        return f"Escritorio en forma de {self.forma} '{self.nombre}' de {self.material}. {cajones} {luz}."