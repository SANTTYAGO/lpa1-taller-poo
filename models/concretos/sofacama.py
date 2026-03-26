"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

from .sofa import Sofa
from .cama import Cama


class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    
    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.
    
    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        """
        Constructor del sofá-cama.
        """
        Sofa.__init__(self, nombre=nombre, material=material, color=color, 
                      precio_base=precio_base, capacidad_personas=capacidad_personas, 
                      tiene_respaldo=True, material_tapizado=material_tapizado, 
                      es_modular=False, incluye_cojines=True)
        
        # 2. En lugar de llamar a Cama.__init__ (que sobreescribiría atributos de Mueble), 
        # inicializamos directamente los atributos específicos que aporta la Cama.
        self.tamaño = tamaño_cama
        self.incluye_colchon = incluye_colchon
        self.tiene_cabecera = False  # Un sofá cama rara vez tiene cabecera clásica
        
        # 3. Atributos únicos del Sofá-Cama
        self.mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"  # Por defecto inicia como sofá

    # --- PROPIEDADES (Getters) ---

    @property
    def mecanismo_conversion(self) -> str:
        return self._mecanismo_conversion
    
    @property
    def modo_actual(self) -> str:
        return self._modo_actual
    
    # --- VALIDACIONES (Setters) ---

    @mecanismo_conversion.setter
    def mecanismo_conversion(self, valor: str):
        if not valor.strip():
            raise ValueError("El mecanismo de conversión no puede estar vacío.")
        self._mecanismo_conversion = valor.lower()

    # --- MÉTODOS DE LÓGICA ---
    
    def alternar_modo(self) -> str:
        """Cambia el estado del mueble entre sofá y cama."""
        if self._modo_actual == "sofa":
            self._modo_actual = "cama"
            return "Se ha desplegado el mecanismo. Ahora es una cama."
        else:
            self._modo_actual = "sofa"
            return "Se ha plegado el mecanismo. Ahora es un sofá."

    def puede_usar_como_cama(self) -> bool:
        """Verifica si actualmente puede usarse como cama."""
        return self._modo_actual == "cama"
    
    def puede_usar_como_sofa(self) -> bool:
        """Verifica si actualmente puede usarse como sofá."""
        return self._modo_actual == "sofa"
    
    def calcular_precio(self) -> float:
        """
        Calcula el precio combinando las funcionalidades de sofá y cama.
        
        Returns:
            float: Precio final del sofá-cama
        """
        # Partimos de un cálculo base mixto
        precio = self.precio_base * 1.5  # Premium por ser dual
        
        # Sumamos lógicas parciales de sus ancestros sin llamar directamente a sus métodos
        # para evitar conflictos de sobre-cálculo
        precio += (self.capacidad_personas * 60.0)
        
        if self.incluye_colchon:
            precio += 150.0
            
        if self.mecanismo_conversion == "hidraulico":
            precio += 120.0  # El mecanismo hidráulico es más costoso
            
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Descripción que combina características de sofá y cama.
        """
        desc = f"Sofá-Cama '{self.nombre}' de {self.material} ({self.color}).\n"
        desc += f"Modo actual: {self.modo_actual.upper()}.\n"
        desc += f"Como Sofá: {self.capacidad_personas} plazas, tapizado en {self.material_tapizado}.\n"
        desc += f"Como Cama: Tamaño {self.tamaño}, "
        desc += "con colchón incluido.\n" if self.incluye_colchon else "sin colchón.\n"
        desc += f"Mecanismo: {self.mecanismo_conversion.capitalize()}."
        
        return desc
    
    def obtener_capacidad_total(self) -> dict:
        """
        Obtiene la capacidad tanto como sofá como cama.
        """
        capacidad_cama = 2 if self.tamaño in ["matrimonial", "queen", "king"] else 1
        return {
            "como_sofa": self.capacidad_personas,
            "como_cama": capacidad_cama
        }
    
    def __str__(self) -> str:
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        return f"Sofá-Cama '{self.nombre}' - Modo actual: {self.modo_actual}"

