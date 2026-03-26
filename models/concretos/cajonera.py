"""
Clase concreta Cajonera.
"""
from ..categorias.almacenamiento import Almacenamiento

class Cajonera(Almacenamiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 num_cajones: int, tiene_ruedas: bool = False):
        
        volumen_estimado = 40.0 * num_cajones
        super().__init__(nombre, material, color, precio_base, volumen_estimado, num_cajones, False)
        
        self.num_cajones = num_cajones
        self.tiene_ruedas = tiene_ruedas

    # --- PROPIEDADES (Getters) ---
    
    @property
    def num_cajones(self) -> int:
        return self._num_cajones
    
    @property
    def tiene_ruedas(self) -> bool:
        return self._tiene_ruedas
    
    # --- VALIDACIONES (Setters) ---

    @num_cajones.setter
    def num_cajones(self, valor: int):
        if valor < 1: raise ValueError("Una cajonera debe tener al menos 1 cajón.")
        self._num_cajones = valor

    @tiene_ruedas.setter
    def tiene_ruedas(self, valor: bool):
        self._tiene_ruedas = valor

    # --- MÉTODOS DE LÓGICA ---

    def calcular_precio(self) -> float:
        precio = self.precio_base + (self.num_cajones * 15.0)
        if self.tiene_ruedas:
            precio += 25.0
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        ruedas = "con ruedas" if self.tiene_ruedas else "sin ruedas"
        return f"Cajonera '{self.nombre}' de {self.material} ({self.color}) {ruedas}, con {self.num_cajones} cajones."