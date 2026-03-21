"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""

from ..mueble import Mueble
from abc import abstractmethod

class Asiento(Mueble):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.
    Hereda de Mueble y añade características específicas de los asientos.
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool, material_tapizado: str = None):
        
        # Llamada al constructor del padre (Mueble)
        super().__init__(nombre, material, color, precio_base)
        
        # Atributos específicos con encapsulación
        self._capacidad_personas = capacidad_personas
        self._tiene_respaldo = tiene_respaldo
        self._material_tapizado = material_tapizado
    
    # --- PROPIEDADES (Getters) ---

    @property
    def capacidad_personas(self) -> int:
        return self._capacidad_personas

    @property
    def tiene_respaldo(self) -> bool:
        return self._tiene_respaldo

    @property
    def material_tapizado(self) -> str:
        return self._material_tapizado
    
    # --- VALIDACIONES (Setters) ---

    @capacidad_personas.setter
    def capacidad_personas(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La capacidad de personas debe ser un número entero positivo.")
        self._capacidad_personas = valor

    @tiene_respaldo.setter
    def tiene_respaldo(self, valor: bool):
        if not isinstance(valor, bool):
            raise ValueError("El campo tiene_respaldo debe ser un valor booleano.")
        self._tiene_respaldo = valor

    @material_tapizado.setter
    def material_tapizado(self, valor: str):
        # El tapizado puede ser None si el mueble no es tapizado
        if valor is not None and not isinstance(valor, str):
            raise ValueError("El material de tapizado debe ser una cadena de texto.")
        self._material_tapizado = valor

    # --- MÉTODOS DE LÓGICA ---
    
    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.
        Este es un método concreto que pueden usar las clases hijas.
        """
        
        factor = 1.0
        
        if self.tiene_respaldo:
            factor += 0.1
        
        if self.material_tapizado:
            mat = self.material_tapizado.lower()
            if mat == "cuero":
                factor += 0.2
            elif mat == "tela":
                factor += 0.1
                
        # Bonus por tamaño (más capacidad suele implicar más espacio/comodidad)
        if self.capacidad_personas > 2:
            factor += 0.1
            
        return factor
    
    def obtener_info_asiento(self) -> str:
        """
        Obtiene información específica del asiento.
        Método concreto auxiliar para las clases hijas.
        """
        info = f"Capacidad: {self.capacidad_personas} pers."
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        if self.material_tapizado:
            info += f", Tapizado: {self.material_tapizado}"
        else:
            info += ", Sin tapizado"
        return info