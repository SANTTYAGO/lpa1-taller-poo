"""
Clase abstracta para muebles de almacenamiento.
"""

from ..mueble import Mueble

class Almacenamiento(Mueble):
    """
    Clase abstracta para muebles destinados a guardar objetos (armarios, cajoneras).
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_volumen: float, numero_compartimentos: int, tiene_puertas: bool):
        
        super().__init__(nombre, material, color, precio_base)
        
        self._capacidad_volumen = capacidad_volumen
        self._numero_compartimentos = numero_compartimentos
        self._tiene_puertas = tiene_puertas

    # --- PROPIEDADES (Getters) ---

    @property
    def capacidad_volumen(self) -> float:
        return self._capacidad_volumen
    
    @property
    def numero_compartimentos(self) -> int:
        return self._numero_compartimentos

    @property
    def tiene_puertas(self) -> bool:
        return self._tiene_puertas
    
    # --- VALIDACIONES (Setters) ---

    @capacidad_volumen.setter
    def capacidad_volumen(self, valor: float):
        if valor <= 0:
            raise ValueError("El volumen debe ser mayor a cero.")
        self._capacidad_volumen = valor

    @numero_compartimentos.setter
    def numero_compartimentos(self, valor: int):
        if valor < 1:
            raise ValueError("Debe tener al menos 1 compartimento.")
        self._numero_compartimentos = valor

    @tiene_puertas.setter
    def tiene_puertas(self, valor: bool):
        self._tiene_puertas = valor

    # --- MÉTODOS DE LÓGICA ---

    def calcular_eficiencia_espacio(self) -> float:
        """Calcula qué tan eficiente es el mueble según sus compartimentos."""
        return self._capacidad_volumen / max(1, self._numero_compartimentos)

    def obtener_info_almacenamiento(self) -> str:
        puertas = "con puertas" if self._tiene_puertas else "abierto"
        return f"Volumen: {self._capacidad_volumen}L, Compartimentos: {self._numero_compartimentos} ({puertas})"