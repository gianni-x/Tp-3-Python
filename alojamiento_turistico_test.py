import unittest
from alojamiento_turistico import AlojamientoTuristico


class TestAlojamientoTuristico(unittest.TestCase):
    def setUp(self):
        # AlojamientoTuristico de prueba con minúsculas.
        self.a0:AlojamientoTuristico = AlojamientoTuristico(1.01234567, 2.01234567, 'nom0', 'nom_calle0', 0, 'tel0', 'mail0')
        # AlojamientoTuristico de prueba con valores inventados, con email y con telefono.
        self.a1:AlojamientoTuristico = AlojamientoTuristico(1.11234567, 2.11234567, 'NOM1', 'NOM_CALLE1', 1, 'TEL1', 'MAIL1')
        # AlojamientoTuristico de prueba con valores inventados, con email y sin telefono.
        self.a2:AlojamientoTuristico = AlojamientoTuristico(1.21234567, 2.21234567, 'NOM2', 'NOM_CALLE2', 2, '', 'MAIL2')
        # AlojamientoTuristico de prueba con valores inventados, sin email y con telefono.
        self.a3:AlojamientoTuristico = AlojamientoTuristico(1.31234567, 2.31234567, 'NOM3', 'NOM_CALLE3', 3, 'TEL3', '')
        # AlojamientoTuristico de prueba con valores inventados, sin email y sin telefono.
        self.a4:AlojamientoTuristico = AlojamientoTuristico(1.41234567, 2.41234567, 'NOM4', 'NOM_CALLE4', 4, '', '')

    def test_coordenadas(self):
        self.assertAlmostEqual(self.a0.longitud, 1.01234567, places=6)
        self.assertAlmostEqual(self.a1.longitud, 1.11234567, places=6)
        self.assertAlmostEqual(self.a2.longitud, 1.21234567, places=6)
        self.assertAlmostEqual(self.a3.longitud, 1.31234567, places=6)
        self.assertAlmostEqual(self.a4.longitud, 1.41234567, places=6)
        self.assertAlmostEqual(self.a0.latitud, 2.01234567, places=6)
        self.assertAlmostEqual(self.a1.latitud, 2.11234567, places=6)
        self.assertAlmostEqual(self.a2.latitud, 2.21234567, places=6)
        self.assertAlmostEqual(self.a3.latitud, 2.31234567, places=6)
        self.assertAlmostEqual(self.a4.latitud, 2.41234567, places=6)

    def test_atributo_nombre(self):
        self.assertEqual(self.a0.nombre, 'NOM0')
        self.assertEqual(self.a1.nombre, 'NOM1')
        self.assertEqual(self.a2.nombre, 'NOM2')
        self.assertEqual(self.a3.nombre, 'NOM3')
        self.assertEqual(self.a4.nombre, 'NOM4')

    def test_direccion(self):
        self.assertEqual(self.a0.calle_nombre, 'nom_calle0')
        self.assertEqual(self.a1.calle_nombre, 'NOM_CALLE1')
        self.assertEqual(self.a2.calle_nombre, 'NOM_CALLE2')
        self.assertEqual(self.a3.calle_nombre, 'NOM_CALLE3')
        self.assertEqual(self.a4.calle_nombre, 'NOM_CALLE4')
        self.assertEqual(self.a0.calle_altura, 0)
        self.assertEqual(self.a1.calle_altura, 1)
        self.assertEqual(self.a2.calle_altura, 2)
        self.assertEqual(self.a3.calle_altura, 3)
        self.assertEqual(self.a4.calle_altura, 4)

    def test_atributo_telefono(self):
        self.assertEqual(self.a0.telefono, 'tel0')
        self.assertEqual(self.a1.telefono, 'TEL1')
        self.assertEqual(self.a2.telefono, 'N/D')
        self.assertEqual(self.a3.telefono, 'TEL3')
        self.assertEqual(self.a4.telefono, 'N/D')

    def test_atributo_email(self):
        self.assertEqual(self.a0.email, 'mail0')
        self.assertEqual(self.a1.email, 'MAIL1')
        self.assertEqual(self.a2.email, 'MAIL2')
        self.assertEqual(self.a3.email, 'N/D')
        self.assertEqual(self.a4.email, 'N/D')

    def test_contacto(self):
        self.assertEqual(self.a0.contacto(), 'tel0 | mail0')
        self.assertEqual(self.a1.contacto(), 'TEL1 | MAIL1')
        self.assertEqual(self.a2.contacto(), 'MAIL2')
        self.assertEqual(self.a3.contacto(), 'TEL3')
        self.assertEqual(self.a4.contacto(), 'N/D')

    def test_distancia(self):
        self.assertAlmostEqual(self.a0.distancia(2.01234567, 1.01234567), 0.0, places=2)
        self.assertAlmostEqual(self.a1.distancia(2.11234567, 1.11234567), 0.0, places=2)
        self.assertAlmostEqual(self.a2.distancia(2.21234567, 1.21234567), 0.0, places=2)
        self.assertAlmostEqual(self.a3.distancia(2.31234567, 1.31234567), 0.0, places=2)
        self.assertAlmostEqual(self.a4.distancia(2.41234567, 1.41234567), 0.0, places=2)
        self.assertAlmostEqual(self.a1.distancia(0, 0), 265445.655417096, places=2)
        self.assertAlmostEqual(self.a2.distancia(2.12, 5.43), 468759.5577475617, places=2)
        self.assertAlmostEqual(self.a3.distancia(0, 0), 295625.425838796, places=2)
        self.assertAlmostEqual(self.a4.distancia(2.12, 5.43), 447575.44150826486, places=2)

    def test_str(self):
        self.assertEqual(str(self.a0), 'ALOJAMIENTO:NOM0')
        self.assertEqual(str(self.a1), 'ALOJAMIENTO:NOM1')
        self.assertEqual(str(self.a2), 'ALOJAMIENTO:NOM2')
        self.assertEqual(str(self.a3), 'ALOJAMIENTO:NOM3')
        self.assertEqual(str(self.a4), 'ALOJAMIENTO:NOM4')

#####################################################################

unittest.main()
