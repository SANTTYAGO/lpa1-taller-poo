"""
Pruebas unitarias para las clases de composición.
"""

import pytest
from models.concretos.mesa import Mesa
from models.concretos.silla import Silla
from models.composicion.comedor import Comedor

class TestComposicionComedor:
    def setup_method(self):
        self.mesa = Mesa("Mesa Test", "Madera", "Roble", 500.0, "rectangular", 6)
        self.silla1 = Silla("Silla 1", "Madera", "Roble", 120.0)
        self.silla2 = Silla("Silla 2", "Madera", "Roble", 120.0)
        self.comedor = Comedor("Comedor Test", self.mesa, [self.silla1, self.silla2])

    def test_creacion_y_agregacion(self):
        """Verifica que el comedor se instancie con sus partes correctamente."""
        assert self.comedor.nombre == "Comedor Test"
        assert len(self.comedor.sillas) == 2
        
        silla3 = Silla("Silla 3", "Madera", "Roble", 120.0)
        self.comedor.agregar_silla(silla3)
        assert len(self.comedor.sillas) == 3

    def test_calculo_precio_total(self):
        """Verifica la suma delegada de los precios de sus componentes."""
        # Mesa de 6 personas (500 * 1.2 = 600) + 2 Sillas (120 * factor 1.1 = 132 c/u) = 600 + 264 = 864
        assert self.comedor.calcular_precio_total() == 864.0
        
    def test_descuento_por_set_completo(self):
        """Verifica la lógica de negocio: 5% descuento si hay 4 o más sillas."""
        self.comedor.agregar_silla(Silla("Silla 3", "Madera", "Roble", 120.0))
        self.comedor.agregar_silla(Silla("Silla 4", "Madera", "Roble", 120.0))
        # Mesa (600) + 4 Sillas (528) = 1128.
        # Descuento del 5%: 1128 * 0.95 = 1071.6
        assert self.comedor.calcular_precio_total() == 1071.6