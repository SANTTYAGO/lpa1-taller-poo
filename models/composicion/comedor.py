"""
Clase Comedor que implementa composición.
Un comedor está compuesto por una mesa y varias sillas.
"""

from ..concretos.mesa import Mesa
from ..concretos.silla import Silla
from typing import List



class Comedor:
    """
    Clase que implementa composición conteniendo una mesa y sillas.
    
    Un comedor es un conjunto de muebles que trabajan juntos.
    La relación es de composición porque el comedor "tiene" una mesa
    y "tiene" sillas, pero estas pueden existir independientemente.
    
    Conceptos OOP aplicados:
    - Composición: El comedor contiene otros objetos (mesa y sillas)
    - Agregación: Los objetos contenidos pueden existir independientemente
    - Encapsulación: Controla el acceso a los componentes internos
    - Abstracción: Simplifica la gestión de múltiples muebles
    """
    
    def __init__(self, nombre: str, mesa: 'Mesa', sillas: List['Silla'] = None):
        """
        Constructor del comedor.
        """
        # Encapsulación de los componentes
        self._nombre = nombre
        self._mesa = mesa
        # Si no se pasan sillas, inicializamos una lista vacía
        self._sillas = sillas if sillas is not None else []

    # --- PROPIEDADES (Getters) ---
    
    @property   
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def mesa(self) -> 'Mesa':
        return self._mesa
    
    @property
    def sillas(self) -> List['Silla']:
        # Retorna una copia para proteger la lista interna de modificaciones directas
        return self._sillas.copy()

    # --- VALIDACIONES (Setters) ---
    # --- MÉTODOS DE LÓGICA ---
    
    def agregar_silla(self, silla: 'Silla') -> str:
        """
        Agrega una silla al comedor.
        """
        if not isinstance(silla, Silla):
            return "Error: Solo se pueden agregar objetos de tipo Silla."
        
        capacidad_maxima = self._calcular_capacidad_maxima()
        if len(self._sillas) >= capacidad_maxima:
            return f"No se pueden agregar más sillas. Capacidad máxima: {capacidad_maxima}."
        
        self._sillas.append(silla)
        return f"Silla '{silla.nombre}' agregada exitosamente al comedor."
    
    def quitar_silla(self, indice: int = -1) -> str:
        """
        Quita una silla del comedor.
        """
        if not self._sillas:
            return "Error: No hay sillas para quitar."
        
        try:
            silla_removida = self._sillas.pop(indice)
            return f"Silla '{silla_removida.nombre}' removida del comedor."
        except IndexError:
            return "Error: Índice de silla inválido."
            
    def calcular_precio_total(self) -> float:
        """
        Calcula el precio total del comedor sumando todos sus componentes.
        """
        # Calculamos usando el método de los objetos internos
        precio_total = self._mesa.calcular_precio()
        
        for silla in self._sillas:
            precio_total += silla.calcular_precio()
        
        # Lógica de negocio: 5% de descuento si es un set completo de 4 o más sillas
        if len(self._sillas) >= 4:
            precio_total *= 0.95
            
        return round(precio_total, 2)
    
    def obtener_descripcion_completa(self) -> str:
        """
        Obtiene una descripción completa del comedor y todos sus componentes.
        """
        desc = f"=== COMEDOR {self.nombre.upper()} ===\n\n"
        
        desc += "MESA:\n"
        desc += f"- {self._mesa.obtener_descripcion()}\n\n"
        
        desc += f"SILLAS ({len(self._sillas)} unidades):\n"
        if not self._sillas:
            desc += "- Ninguna incluida.\n"
        else:
            for i, silla in enumerate(self._sillas, 1):
                desc += f"{i}. {silla.obtener_descripcion()}\n"
                
        desc += f"\n--- PRECIO TOTAL: ${self.calcular_precio_total():,.2f} ---"
        if len(self._sillas) >= 4:
            desc += "\n(Incluye 5% de descuento por set completo)"
            
        return desc
    
    def _calcular_capacidad_maxima(self) -> int:
        """
        Calcula la capacidad máxima de sillas basada en el tamaño de la mesa.
        Método privado auxiliar.
        """
        # Ya que nuestra clase Mesa tiene el atributo 'capacidad_personas', lo usamos:
        if hasattr(self._mesa, 'capacidad_personas'):
            return self._mesa.capacidad_personas
        return 6 # Valor por defecto seguro
    
    def obtener_resumen(self) -> dict:
        """
        Obtiene un resumen estadístico del comedor.
        """
        return {
            "nombre": self.nombre,
            "total_muebles": len(self),  # Usa el método mágico __len__
            "precio_mesa": self._mesa.calcular_precio(),
            "precio_sillas": sum(s.calcular_precio() for s in self._sillas),
            "precio_total": self.calcular_precio_total(),
            "capacidad_personas": len(self._sillas),
            "materiales_utilizados": self._obtener_materiales_unicos()
        }
    
    def _obtener_materiales_unicos(self) -> list:
        """
        Obtiene una lista de materiales únicos usados en el comedor.
        Método privado auxiliar.
        """
        # Usamos un Set para que los materiales no se repitan
        materiales = {self._mesa.material}
        
        for silla in self._sillas:
            materiales.add(silla.material)
            # Si la silla tiene tapizado (es un atributo de la clase Asiento)
            if hasattr(silla, 'material_tapizado') and silla.material_tapizado:
                materiales.add(silla.material_tapizado)
                
        return list(materiales)
    
    def __str__(self) -> str:
        return f"Comedor '{self.nombre}': Mesa de {self._mesa.material} + {len(self._sillas)} sillas."
    
    def __len__(self) -> int:
        """Permite hacer len(mi_comedor) para saber cuántos muebles tiene."""
        return 1 + len(self._sillas) # 1 (la mesa) + cantidad de sillas

