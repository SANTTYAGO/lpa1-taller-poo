"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

from ..categorias.asientos import Asiento


class Silla(Asiento):
    """
    Clase concreta que representa una silla.
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)
        
        self.altura_regulable = altura_regulable
        self.tiene_ruedas = tiene_ruedas
    
    # --- PROPIEDADES (Getters) ---

    @property
    def altura_regulable(self) -> bool:
        return self._altura_regulable
    
    @property
    def tiene_ruedas(self) -> bool:
        return self._tiene_ruedas
    
    # --- VALIDACIONES (Setters) ---

    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        self._altura_regulable = value

    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        self._tiene_ruedas = value

    # --- MÉTODOS DE LÓGICA ---
    # --- IMPLEMENTACIÓN DE MÉTODOS ABSTRACTOS (Polimorfismo) ---
    
    def calcular_precio(self) -> float:
        """Calcula el precio final aplicando factores y características extra."""
        # 1. Comenzar con el precio base y aplicar factor de comodidad heredado
        precio_final = self.precio_base * self.calcular_factor_comodidad()
        
        # 2. Agregar costos por características especiales
        if self.altura_regulable:
            precio_final += 45.0  # Costo adicional por pistón de altura
        if self.tiene_ruedas:
            precio_final += 25.0  # Costo adicional por set de ruedas
            
        # 3. Retornar precio redondeado a 2 decimales
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """Crea y retorna una descripción detallada."""
        desc = f"Silla '{self.nombre}' de {self.material} ({self.color}).\n"
        desc += f"Detalles: {self.obtener_info_asiento()}.\n"
        
        extras = []
        if self.altura_regulable: extras.append("altura regulable")
        if self.tiene_ruedas: extras.append("ruedas")
        
        if extras:
            desc += f"Extras: {', '.join(extras).capitalize()}."
        else:
            desc += "Extras: Ninguno."
            
        return desc
    
    # --- MÉTODOS ESPECÍFICOS DE LA SILLA ---

    def regular_altura(self, nueva_altura: int) -> str:
        """Simula la regulación de altura si el mecanismo existe."""
        if not self.altura_regulable:
            return "Esta silla no tiene mecanismo para regular la altura."
        if nueva_altura < 40 or nueva_altura > 80:
            return "Altura fuera de los límites permitidos (40cm - 80cm)."
        return f"Altura ajustada exitosamente a {nueva_altura}cm."
    
    def es_silla_oficina(self) -> bool:
        """Determina si la silla es adecuada para oficina."""
        # Una silla es de oficina si tiene ruedas Y altura regulable
        return self.altura_regulable and self.tiene_ruedas

