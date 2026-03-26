"""
Clase concreta Armario.
"""
from ..categorias.almacenamiento import Almacenamiento

class Armario(Almacenamiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 num_puertas: int, num_cajones: int, tiene_espejos: bool = False):
        
        # Un armario es un almacenamiento grande, estimamos un volumen base.
        volumen_estimado = 500.0 * num_puertas
        super().__init__(nombre, material, color, precio_base, volumen_estimado, num_puertas + num_cajones, True)
        
        self.num_puertas = num_puertas
        self.num_cajones = num_cajones
        self.tiene_espejos = tiene_espejos

    # --- PROPIEDADES (Getters) ---

    @property
    def num_puertas(self) -> int:
        return self._num_puertas

    @property
    def num_cajones(self) -> int:
        return self._num_cajones
    
    @property
    def tiene_espejos(self) -> bool:
        return self._tiene_espejos
    

    # --- VALIDACIONES (Setters) ---

    @num_puertas.setter
    def num_puertas(self, valor: int):
        if valor < 1: raise ValueError("Un armario debe tener al menos 1 puerta.")
        self._num_puertas = valor
    
    @num_cajones.setter
    def num_cajones(self, valor: int):
        self._num_cajones = max(0, valor)
    
    @tiene_espejos.setter
    def tiene_espejos(self, valor: bool):
        self._tiene_espejos = valor

    # --- MÉTODOS DE LÓGICA ---

    def calcular_precio(self) -> float:
        precio = self.precio_base
        precio += self.num_puertas * 30.0
        precio += self.num_cajones * 20.0
        if self.tiene_espejos:
            precio += 75.0
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        espejos = "con espejos" if self.tiene_espejos else "sin espejos"
        desc = f"Armario '{self.nombre}' de {self.material} ({self.color}) {espejos}.\n"
        desc += f"Detalles: {self.num_puertas} puertas, {self.num_cajones} cajones. {self.obtener_info_almacenamiento()}."
        return desc