import unittest
from establecimiento_gastronomico import EstablecimientoGastronomico

class TestEstablecimientoGastronomico(unittest.TestCase):
    def setUp(self):
        # EstablecimientoGastronomico de prueba con valores inventados.
        self.eg:EstablecimientoGastronomico = EstablecimientoGastronomico(1.2, 3.4, 'NOM_EG', 'RUB_EG', 'CALLE_NOM', 1234)

    def test_atributos_str(self):
        self.assertEqual(self.eg.nombre, 'NOM_EG')
        self.assertEqual(self.eg.rubro, 'RUB_EG')
        self.assertEqual(self.eg.calle_nombre, 'CALLE_NOM')

    def test_atributos_float(self):
        self.assertAlmostEqual(self.eg.longitud, 1.2, places=6)
        self.assertAlmostEqual(self.eg.latitud, 3.4, places=6)

    def test_atributos_int(self):
        self.assertEqual(self.eg.calle_altura, 1234)

    def test_str(self):
        self.assertEqual(str(self.eg), 'NOM_EG@CALLE_NOM 1234')

#####################################################################

unittest.main()
