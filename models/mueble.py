"""
Clase base abstracta Mueble
Este es el punto de partida de nuestra jerarquía de clases.
"""

from abc import ABC, abstractmethod


class Mueble:
    """
    Clase abstracta base para todos los muebles.
    
    Esta clase define la estructura común que deben tener todos los muebles
    de nuestra tienda, pero no puede ser instanciada directamente.
    
    Conceptos OOP aplicados:
    - Abstracción: Define una interfaz común sin implementación específica
    - Encapsulación: Usa atributos privados con getters/setters
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float):
        """
        Constructor de la clase Mueble.
        """
        # Inicialización de atributos protegidos (Encapsulación)
        self._nombre = nombre
        self._material = material
        self._color = color
        self._precio_base = precio_base
    
    # --- PROPIEDADES (Getters) ---
    
    @property
    def nombre(self) -> str:
        """Getter para el nombre del mueble."""
        return self._nombre

    @property
    def material(self) -> str:
        """Getter para el material del mueble."""
        return self._material

    @property
    def color(self) -> str:
        """Getter para el color del mueble."""
        return self._color

    @property
    def precio_base(self) -> float:
        """Getter para el precio base."""
        return self._precio_base
    
    # --- PROPIEDADES (Setters) ---

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser una cadena de texto no vacía.")
        self._nombre = valor

    @material.setter
    def material(self, valor: str):
        self._material = valor

    @color.setter
    def color(self, valor: str):
        self._color = valor

    @precio_base.setter
    def precio_base(self, valor: float):
        if valor < 0:
            raise ValueError("El precio base no puede ser negativo.")
        self._precio_base = float(valor)
    
    # --- MÉTODOS ABSTRACTOS (Polimorfismo) ---

    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final del mueble.
        Debe ser implementado por cada clase concreta (Silla, Mesa, etc.).
        """
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del mueble.
        Debe ser implementado por cada clase concreta.
        """
        pass
    
    # --- MÉTODOS DE REPRESENTACIÓN ---

    def __str__(self) -> str:
        return f"{self.nombre} de {self.material} color {self.color}"
    
    def __repr__(self) -> str:
        return (f"Mueble(nombre='{self.nombre}', material='{self.material}', "
                f"color='{self.color}', precio_base={self.precio_base})")