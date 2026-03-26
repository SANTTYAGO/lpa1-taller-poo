"""
Pruebas unitarias para las clases de muebles.
Estas pruebas validan el correcto funcionamiento de todos los conceptos OOP implementados.
"""

import pytest
from models.mueble import Mueble
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.concretos.sofacama import SofaCama
from models.concretos.sofa import Sofa
from models.concretos.cama import Cama
from models.composicion.comedor import Comedor
from models.categorias.asientos import Asiento
from models.categorias.superficies import Superficie
from services.tienda import TiendaMuebles


class TestMuebleBase:
    """
    Pruebas para la clase base abstracta Mueble.
    Valida conceptos de abstracción y encapsulación.
    """
    
    def test_no_puede_instanciar_mueble_directamente(self):
        """
        Prueba que no se puede instanciar la clase abstracta Mueble directamente.
        Valida el concepto de abstracción.
        """
        with pytest.raises(TypeError):
            mueble = Mueble("Test", "Madera", "Café", 100.0)
    

class TestSilla:
    """
    Pruebas para la clase Silla.
    Valida herencia, polimorfismo y encapsulación.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.silla_basica = Silla(
            nombre="Silla Básica",
            material="Madera",
            color="Café",
            precio_base=150.0,
            tiene_respaldo=True
        )

        self.silla_oficina = Silla(
            nombre="Silla Oficina",
            material="Metal",
            color="Negro",
            precio_base=300.0,
            tiene_respaldo=True,
            material_tapizado="cuero",
            altura_regulable=True,
            tiene_ruedas=True
        )
    
    def test_creacion_silla_basica(self):
        """Prueba la creación correcta de una silla básica."""
        assert self.silla_basica.nombre == "Silla Básica"
        assert self.silla_basica.material == "Madera"
        assert self.silla_basica.color == "Café"
        assert self.silla_basica.precio_base == 150.0
        assert self.silla_basica.tiene_respaldo is True
    
    def test_calculo_precio_silla_basica(self):
        """Prueba el cálculo de precio para silla básica."""
    
        # Implementar test de cálculo de precio
        precio = self.silla_basica.calcular_precio()

        # El precio debe incluir el precio base + factor de comodidad por respaldo
        # Precio base: 150.0
        # Factor comodidad con respaldo: 1.1 (150.0 * 1.1 = 165.0)
        assert precio == 165.0
    
    def test_calculo_precio_silla_oficina(self):
        """Prueba el cálculo de precio para silla de oficina con todas las características."""
        precio = self.silla_oficina.calcular_precio()
        # Base: 300.0
        # Comodidad: 1.0 + 0.1(respaldo) + 0.2(cuero) = 1.3
        # 300 * 1.3 = 390.0
        # Extras: 45.0 (altura) + 25.0 (ruedas) = 70.0
        # Total = 460.0
        assert precio == 460.0
    
    def test_es_silla_oficina(self):
        """Prueba la lógica de identificación de silla de oficina."""
        assert self.silla_basica.es_silla_oficina() is False
        assert self.silla_oficina.es_silla_oficina() is True
    
    def test_regular_altura_silla_sin_mecanismo(self):
        """Prueba que las sillas sin altura regulable no pueden ajustarse."""
        resultado = self.silla_basica.regular_altura(50)
        assert "no tiene mecanismo" in resultado.lower()
    
    def test_regular_altura_silla_con_mecanismo(self):
        """Prueba la regulación de altura en sillas que lo permiten."""
        resultado_valido = self.silla_oficina.regular_altura(60)
        assert "exitosamente" in resultado_valido.lower()
        resultado_invalido = self.silla_oficina.regular_altura(100)
        assert "fuera de los límites" in resultado_invalido.lower()
    
    def test_validaciones_setter(self):
        """Prueba las validaciones en los setters."""

        with pytest.raises(ValueError):
            self.silla_basica.nombre = ""

        with pytest.raises(ValueError):
            self.silla_basica.precio_base = -100

        with pytest.raises(ValueError):
            self.silla_basica.capacidad_personas = 0
    
    def test_obtener_descripcion(self):
        """Prueba que la descripción contenga información relevante."""
        descripcion = self.silla_basica.obtener_descripcion()
        assert "Silla 'Silla Básica'" in descripcion
        assert "Madera" in descripcion
        assert "Ninguno" in descripcion # No tiene extras
    
    def test_polimorfismo_herencia(self):
        """Prueba que la silla implementa correctamente los métodos abstractos."""

        # Debe poder llamarse como Mueble (polimorfismo)
        from models.categorias.asientos import Asiento

        assert isinstance(self.silla_basica, Asiento)
        assert hasattr(self.silla_basica, 'calcular_precio')
        assert hasattr(self.silla_basica, 'obtener_descripcion')

        # Los métodos deben retornar valores válidos
        precio = self.silla_basica.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

        descripcion = self.silla_basica.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


class TestSofaCama:
    """
    Pruebas para la clase SofaCama.
    Valida herencia múltiple y resolución MRO.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.sofacama = SofaCama(
            nombre="SofaCama Deluxe",
            material="Madera",
            color="Azul",
            precio_base=800.0,
            capacidad_personas=3,
            material_tapizado="tela",
            tamaño_cama="matrimonial",
            incluye_colchon=True,
            mecanismo_conversion="plegable"
        )
    
    def test_creacion_sofacama(self):
        """Prueba la creación correcta del sofá-cama."""

        # Implementar test de creación con herencia múltiple
        assert self.sofacama.nombre == "SofaCama Deluxe"
        assert self.sofacama.capacidad_personas == 3
        assert self.sofacama.tamaño_cama == "matrimonial"
        assert self.sofacama.incluye_colchon == True
        assert self.sofacama.mecanismo_conversion == "plegable"
        assert self.sofacama.modo_actual == "sofa"
    
    def test_conversion_modos(self):
        """Prueba la conversión entre modos sofá y cama."""

        # Inicialmente debe estar en modo sofá
        assert self.sofacama.modo_actual == "sofa"

        # Convertir a cama
        resultado = self.sofacama.convertir_a_cama()
        assert "convertido a cama" in resultado.lower()
        assert self.sofacama.modo_actual == "cama"

        # Intentar convertir a cama nuevamente
        resultado2 = self.sofacama.convertir_a_cama()
        assert "ya está en modo cama" in resultado2.lower()

        # Convertir de vuelta a sofá
        resultado3 = self.sofacama.convertir_a_sofa()
        assert "convertida a sofá" in resultado3.lower()
        assert self.sofacama.modo_actual == "sofa"
    
    def test_calculo_precio_dual(self):
        """Prueba el cálculo de precio considerando funcionalidad dual."""
        precio = self.sofacama.calcular_precio()
        # Base * 1.5: 800 * 1.5 = 1200
        # + (capacidad * 60) = 180
        # + 150 (colchon)
        # Total = 1530.0
        assert precio == 1530.0
    
    def test_capacidad_total(self):
        """Prueba las capacidades en ambos modos."""
        capacidades = self.sofacama.obtener_capacidad_total()
        assert capacidades["como_sofa"] == 3
        assert capacidades["como_cama"] == 2
    
    def test_herencia_multiple_mro(self):
        """Prueba que la herencia múltiple funciona correctamente."""

        # Implementar test de MRO (Method Resolution Order)
        from models.concretos.sofa import Sofa
        from models.concretos.cama import Cama

        assert isinstance(self.sofacama, Sofa)
        assert isinstance(self.sofacama, Cama)

        # Verificar que tiene métodos de ambas clases padre
        assert hasattr(self.sofacama, 'convertir_a_cama')
        assert hasattr(self.sofacama, 'convertir_a_sofa')
        assert hasattr(self.sofacama, 'calcular_precio')
        assert hasattr(self.sofacama, 'obtener_descripcion')


class TestComedor:
    """
    Pruebas para la clase Comedor.
    Valida composición y agregación.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""

        # Crear instancias para composición
        self.mesa = Mesa(
            nombre="Mesa Familiar",
            material="Madera",
            color="Roble",
            precio_base=500.0,
            forma="rectangular",
            capacidad_personas=6
        )

        self.silla1 = Silla("Silla 1", "Madera", "Roble", 120.0, True)
        self.silla2 = Silla("Silla 2", "Madera", "Roble", 120.0, True)

        self.comedor = Comedor(
            nombre="Comedor Familiar",
            mesa=self.mesa,
            sillas=[self.silla1, self.silla2]
        )
    
    def test_creacion_comedor(self):
        """Prueba la creación correcta del comedor con composición."""

        # Implementar test de composición
        assert self.comedor.nombre == "Comedor Familiar"
        assert self.comedor.mesa == self.mesa
        assert len(self.comedor.sillas) == 2
        assert self.silla1 in self.comedor.sillas
        assert self.silla2 in self.comedor.sillas
    
    def test_agregar_silla(self):
        """Prueba agregar sillas al comedor."""
        silla_nueva = Silla("Silla Nueva", "Madera", "Roble", 120.0, True)
        resultado = self.comedor.agregar_silla(silla_nueva)
        assert "exitosamente" in resultado.lower()
        assert len(self.comedor.sillas) == 3
        assert silla_nueva in self.comedor.sillas
    
    def test_agregar_objeto_invalido(self):
        """Prueba que no se pueden agregar objetos que no sean sillas."""
        mesa_falsa = Mesa("Mesa", "Madera", "Roble", 500, "cuadrada", 4)
        resultado = self.comedor.agregar_silla(mesa_falsa)
        assert "Error:" in resultado
        assert len(self.comedor.sillas) == 2 # No se agregó
    
    def test_quitar_silla(self):
        """Prueba quitar sillas del comedor."""
        resultado = self.comedor.quitar_silla(0)
        assert "removida" in resultado.lower()
        assert len(self.comedor.sillas) == 1
        
        # Probar remover con índice inválido
        resultado_invalido = self.comedor.quitar_silla(99)
        assert "Error:" in resultado_invalido
    
    def test_calculo_precio_total(self):
        """Prueba el cálculo del precio total del comedor."""
        # Mesa (6 pers) = 500 * 1.2 = 600
        # 2 Sillas = (120 * 1.1) * 2 = 132 * 2 = 264
        # Total = 864
        assert self.comedor.calcular_precio_total() == 864.0
    
    def test_descuento_set_completo(self):
        """Prueba el descuento por set completo (4+ sillas)."""
        # Añadimos 2 sillas más para llegar a 4
        self.comedor.agregar_silla(Silla("Silla 3", "Madera", "Roble", 120.0, True))
        self.comedor.agregar_silla(Silla("Silla 4", "Madera", "Roble", 120.0, True))
        
        # Mesa = 600
        # 4 Sillas = 132 * 4 = 528
        # Subtotal = 1128
        # Descuento 5% (1128 * 0.95) = 1071.6
        assert self.comedor.calcular_precio_total() == 1071.6
    
    def test_descripcion_completa(self):
        """Prueba la generación de descripción completa."""
        desc = self.comedor.obtener_descripcion_completa()
        assert "COMEDOR COMEDOR FAMILIAR" in desc
        assert "MESA:" in desc
        assert "SILLAS (2 unidades):" in desc
    
    def test_resumen_estadistico(self):
        """Prueba la generación de resumen estadístico."""
        resumen = self.comedor.obtener_resumen()
        assert resumen["total_muebles"] == 3
        assert resumen["capacidad_personas"] == 2
        assert "Madera" in resumen["materiales_utilizados"]
    
    def test_len_comedor(self):
        """Prueba el método __len__ del comedor."""
        assert len(self.comedor) == 3 # 1 mesa + 2 sillas


class TestConceptosOOPGenerales:
    """
    Pruebas que validan conceptos generales de OOP aplicados en todo el sistema.
    """
    
    def test_polimorfismo_general(self):
        """Prueba que diferentes tipos de muebles implementan polimorfismo correctamente."""
        for mueble in muebles_de_prueba.values():
            assert hasattr(mueble, 'calcular_precio')
            assert hasattr(mueble, 'obtener_descripcion')
            assert isinstance(mueble.calcular_precio(), float)
            assert isinstance(mueble.obtener_descripcion(), str)
    
    def test_encapsulacion_general(self):
        """Prueba que la encapsulación funciona correctamente."""
        silla = muebles_de_prueba['silla_basica']
        # No se debe acceder a atributos protegidos directamente en buenas prácticas
        # pero verificamos que las propiedades existen
        assert hasattr(silla, 'nombre')
        assert hasattr(silla, 'precio_base')
    
    def test_herencia_jerarquia(self):
        """Prueba que la jerarquía de herencia funciona correctamente."""
        mesa = muebles_de_prueba['mesa_basica']
        assert isinstance(mesa, Superficie)
        # La mesa no hereda directamente de Mueble en tu estructura 
        # (pero Superficie sí hereda de Mueble, es válido)


# Agregar fixture para datos de prueba si es necesario
@pytest.fixture
def muebles_de_prueba():
    """Fixture que proporciona muebles de prueba para múltiples tests."""
    return {
        'silla_basica': Silla("Silla Test", "Madera", "Café", 100.0, True),
        'mesa_basica': Mesa("Mesa Test", "Madera", "Roble", 300.0, "rectangular", 4),
        'sofacama': SofaCama("SofaCama Test", "Tela", "Gris", 800.0)
    }


class TestIntegracion:
    """
    Pruebas de integración que validan el funcionamiento conjunto de múltiples clases.
    """
    
    def test_creacion_tienda_completa(self):
        """Prueba la creación de una tienda con múltiples tipos de muebles."""
        tienda = TiendaMuebles("Tienda Test")

        # Agregar a la tienda
        tienda.agregar_mueble(muebles_de_prueba['silla_basica'])
        tienda.agregar_mueble(muebles_de_prueba['mesa_basica'])
        
        assert tienda.total_muebles == 2

        # Verificar búsquedas
        resultados_madera = tienda.filtrar_por_material("Madera")
        assert len(resultados_madera) == 2
        
        resultados_nombre = tienda.buscar_muebles_por_nombre("Silla")
        assert len(resultados_nombre) == 1
        assert resultados_nombre[0].nombre == "Silla Test"
        
        # Verificar cálculos globales
        valor_inventario = tienda.calcular_valor_inventario()
        assert valor_inventario > 0


if __name__ == "__main__":
    # Configurar ejecución de pruebas
    pytest.main([__file__, "-v"])

