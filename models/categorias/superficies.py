"""
Clase abstracta para muebles para superficios de trabajo o del hogar .
"""

from ..mueble import Mueble

class Superficie(Mueble):
    """
    Clase abstracta para muebles con superficies de trabajo o apoyo (mesas, escritorios).
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 ancho: float, largo: float, es_extensible: bool = False):
        super().__init__(nombre, material, color, precio_base)
        self._ancho = ancho
        self._largo = largo
        self._es_extensible = es_extensible

    # --- PROPIEDADES (Getters) ---
    @property
    def ancho(self) -> float:
        return self._ancho
    
    @property
    def largo(self) -> float:
        return self._largo
    
    @property
    def es_extensible(self) -> bool:
        return self._es_extensible

    # --- PROPIEDADES (Setters) ---    
    @ancho.setter
    def ancho(self, valor: float):
        if valor <= 0: raise ValueError("El ancho debe ser positivo.")
        self._ancho = valor

    @largo.setter
    def largo(self, valor: float):
        if valor <= 0: raise ValueError("El largo debe ser positivo.")
        self._largo = valor

    @es_extensible.setter
    def es_extensible(self, valor: bool):
        self._es_extensible = valor

    # --- MÉTODOS DE LÓGICA ---

    def calcular_area(self) -> float:
        area = self._ancho * self._largo
        return area * 1.2 if self._es_extensible else area

    def obtener_info_superficie(self) -> str:
        ext = "es extensible" if self._es_extensible else "fija"
        return f"Dimensiones: {self._ancho}x{self._largo}m (Superficie {ext})"