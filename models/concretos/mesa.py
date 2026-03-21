"""
Clase concreta Mesa.
"""
from ..categorias.superficies import Superficie

class Mesa(Superficie):
    """
    Clase concreta que representa una mesa.
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str, capacidad_personas: int, 
                 ancho: float = 1.0, largo: float = 1.0, tiene_extensiones: bool = False):
        
        super().__init__(nombre, material, color, precio_base, ancho, largo, tiene_extensiones)
        
        self.forma = forma
        self.tiene_extensiones = tiene_extensiones
        self.capacidad_personas = capacidad_personas
    
    # --- PROPIEDADES (Getters) ---

    @property
    def forma(self) -> str:
        return self._forma
    
    @property
    def tiene_extensiones(self) -> bool:
        return self._tiene_extensiones
    
    @property
    def capacidad_personas(self) -> int:
        return self._capacidad_personas
    
    # --- VALIDACIONES (Setters) ---

    @forma.setter
    def forma(self, valor: str):
        if valor.lower() not in ["redonda", "cuadrada", "rectangular", "ovalada"]:
            raise ValueError("Forma de mesa no válida.")
        self._forma = valor.lower()

    @tiene_extensiones.setter
    def tiene_extensiones(self, value: bool) -> None:
        self._tiene_extensiones = value

    @capacidad_personas.setter
    def capacidad_personas(self, valor: int):
        if valor < 1:
            raise ValueError("La mesa debe tener capacidad para al menos 1 persona.")
        self._capacidad_personas = valor

    # --- MÉTODOS DE LÓGICA ---

    def calcular_precio(self) -> float:
        """Calcula el precio basándose en el área y material."""
        precio = self.precio_base
        
        # Cobro extra si es una mesa muy grande
        if self.capacidad_personas >= 6:
            precio *= 1.2
            
        # Cobro extra si es extensible
        if self.es_extensible:
            precio += 100.0
            
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """Descripción específica de la mesa."""
        desc = f"Mesa {self.forma.capitalize()} '{self.nombre}' de {self.material} ({self.color}).\n"
        desc += f"Para {self.capacidad_personas} personas. {self.obtener_info_superficie()}."
        return desc