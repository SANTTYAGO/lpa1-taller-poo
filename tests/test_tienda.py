"""
Pruebas unitarias para la Tienda.
"""

import pytest
from services.tienda import TiendaMuebles
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa

class TestTiendaMuebles:
    def setup_method(self):
        self.tienda = TiendaMuebles("Tienda Test")
        self.silla = Silla("Silla Comedor", "Madera", "Roble", 100.0)
        self.mesa = Mesa("Mesa Comedor", "Madera", "Roble", 400.0, "rectangular", 4)
        
    def test_agregar_y_buscar_muebles(self):
        """Verifica que el inventario funcione y la búsqueda no sea estricta."""
        self.tienda.agregar_mueble(self.silla)
        self.tienda.agregar_mueble(self.mesa)
        
        assert self.tienda.total_muebles == 2
        
        # Búsqueda parcial y en minúsculas
        resultados = self.tienda.buscar_muebles_por_nombre("silla")
        assert len(resultados) == 1
        assert resultados[0].nombre == "Silla Comedor"

    def test_filtrar_por_precio_y_material(self):
        """Verifica los filtros principales de la tienda."""
        self.tienda.agregar_mueble(self.silla)
        self.tienda.agregar_mueble(self.mesa)
        
        baratos = self.tienda.filtrar_por_precio(0, 200)
        assert len(baratos) == 1
        assert baratos[0] == self.silla
        
        madera = self.tienda.filtrar_por_material("Madera")
        assert len(madera) == 2

    def test_aplicar_descuento_y_venta(self):
        """Verifica la lógica de transacciones y descuentos."""
        self.tienda.agregar_mueble(self.silla)
        
        # Aplicamos descuento del 10% a todas las sillas
        self.tienda.aplicar_descuento("silla", 10)
        
        # Realizamos venta
        venta = self.tienda.realizar_venta(self.silla, "Juan Perez")
        
        assert "error" not in venta
        assert venta["cliente"] == "Juan Perez"
        
        # Precio base (100) * factor comodidad (1.1) = 110. 
        # 10% de descuento sobre 110 = 99.0
        assert venta["precio_final"] == 99.0
        
        # El mueble debió salir del inventario
        assert self.tienda.total_muebles == 0 

    def test_estadisticas_y_reporte(self):
        """Verifica la generación de información para dueños de la tienda."""
        self.tienda.agregar_mueble(self.silla)
        stats = self.tienda.obtener_estadisticas()
        
        assert stats["total_muebles"] == 1
        assert stats["valor_inventario"] == 110.0
        
        reporte = self.tienda.generar_reporte_inventario()
        assert "Tienda Test" in reporte
        assert "Total de muebles: 1" in reporte