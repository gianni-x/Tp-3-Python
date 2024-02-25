import unittest, filecmp
from typing import List
from alojamiento_turistico import AlojamientoTuristico
from establecimiento_gastronomico import EstablecimientoGastronomico
from dataset import DataSetTuristico

class TestDataSetTuristico(unittest.TestCase):
    def setUp(self):
        self.ds0:DataSetTuristico = DataSetTuristico('alojamientos_0.csv','est_gastronomicos_0.csv')
        self.ds1:DataSetTuristico = DataSetTuristico('alojamientos_1.csv','est_gastronomicos_1.csv')
        self.ds5:DataSetTuristico = DataSetTuristico('alojamientos_5.csv','est_gastronomicos_5.csv')

        self.at1 = AlojamientoTuristico(-58.373013,-34.618212,'BOLIVAR','BOLIVAR',886,'4361 5105','reservas@hotel-bolivar.com.ar')
        self.at2 = AlojamientoTuristico(-58.374235,-34.619917,'SANTA MARIA DE LA SALUD','PERU',1022,'4307-9593','info@paradorbue.com')
        self.at3 = AlojamientoTuristico(-58.403906,-34.614665,'SPLENDID','BELGRANO ',2688,'4943-0031','ventas@hotel-splendid.com.ar')
        self.at4 = AlojamientoTuristico(-58.383766,-34.613187,'LA CASA DEL MÉDICO','AV. BELGRANO ',1235,'4383-8414','info@lacasadelmedico.com.ar')
        self.at5 = AlojamientoTuristico(-58.390315,-34.621526,'HOTEL 26 DE JULIO','HUMBERTO 1 ',1712,'4305-3030','hotel26dejulio@judiciales.org.ar')

        self.eg1 = EstablecimientoGastronomico(-58.434271,-34.597104,'1893','Restaurante','SCALABRINI ORTIZ, RAUL AV.',701)
        self.eg2 = EstablecimientoGastronomico(-58.372892,-34.597594,'AL CARBÓN','Restaurante','RECONQUISTA',875)
        self.eg3 = EstablecimientoGastronomico(-58.411435,-34.588835,'ANASAGASTI','Restaurante','ANASAGASTI',2067)
        self.eg4 = EstablecimientoGastronomico(-58.374516,-34.612552,'BAR EL COLONIAL','Bar Notable','BELGRANO AV.',599)
        self.eg5 = EstablecimientoGastronomico(-58.392357,-34.604902,'BAR LA ACADEMIA','Bar Notable','CALLAO AV.',368)

    def test_establecimientos(self):
        self.assertEqual(self.ds0.alojamientos(),[])
        self.assertEqual(self.ds1.alojamientos(),[self.at1])
        self.assertEqual(self.ds5.alojamientos(),[self.at1,self.at5,self.at4,self.at2,self.at3])

    def test_alojamiento_por_nombre(self):
        self.assertEqual(self.ds5.alojamiento_por_nombre('BOLIVAR'),self.at1)
        self.assertEqual(self.ds5.alojamiento_por_nombre('SANTA MARIA DE LA SALUD'),self.at2)
        self.assertEqual(self.ds5.alojamiento_por_nombre('SPLENDID'),self.at3)
        self.assertEqual(self.ds5.alojamiento_por_nombre('LA CASA DEL MÉDICO'),self.at4)
        self.assertEqual(self.ds5.alojamiento_por_nombre('HOTEL 26 DE JULIO'),self.at5)

    def test_tres_boliches_cercanos(self):
        self.assertEqual(self.ds5.tres_boliches_cercanos(self.at1), (self.eg4,self.eg2,self.eg5))
        self.assertEqual(self.ds5.tres_boliches_cercanos(self.at2), (self.eg4,self.eg5,self.eg2))
        self.assertEqual(self.ds5.tres_boliches_cercanos(self.at3), (self.eg5,self.eg4,self.eg3))
        self.assertEqual(self.ds5.tres_boliches_cercanos(self.at4), (self.eg4,self.eg5,self.eg2))
        self.assertEqual(self.ds5.tres_boliches_cercanos(self.at5), (self.eg4,self.eg5,self.eg2))

    def test_boliche_proximo_de_rubro(self):
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at1,'Restaurante'),self.eg2)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at2,'Restaurante'),self.eg2)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at3,'Restaurante'),self.eg3)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at4,'Restaurante'),self.eg2)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at5,'Restaurante'),self.eg2)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at1,'Bar Notable'),self.eg4)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at2,'Bar Notable'),self.eg4)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at3,'Bar Notable'),self.eg5)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at4,'Bar Notable'),self.eg4)
        self.assertEqual(self.ds5.boliche_proximo_de_rubro(self.at5,'Bar Notable'),self.eg4)

    def test_rubros_en_zona(self):
        self.assertEqual(self.ds1.rubros_en_zona(self.at1,1000),set())
        self.assertEqual(self.ds1.rubros_en_zona(self.at1,10000),{'Restaurante'})
        self.assertEqual(self.ds5.rubros_en_zona(self.at1,1000),{'Bar Notable'})
        self.assertEqual(self.ds5.rubros_en_zona(self.at1,10000),{'Restaurante','Bar Notable'})
        self.assertEqual(self.ds5.rubros_en_zona(self.at2,1000),{'Bar Notable'})
        self.assertEqual(self.ds5.rubros_en_zona(self.at2,10000),{'Restaurante','Bar Notable'})
        self.assertEqual(self.ds5.rubros_en_zona(self.at3,1000),set())
        self.assertEqual(self.ds5.rubros_en_zona(self.at3,10000),{'Restaurante','Bar Notable'})
        self.assertEqual(self.ds5.rubros_en_zona(self.at4,1000),{'Bar Notable'})
        self.assertEqual(self.ds5.rubros_en_zona(self.at4,10000),{'Restaurante','Bar Notable'})
        self.assertEqual(self.ds5.rubros_en_zona(self.at5,1000),set())
        self.assertEqual(self.ds5.rubros_en_zona(self.at5,10000),{'Restaurante','Bar Notable'})

    def test_exportar_cercanos(self):
        self.ds5.exportar_cercanos('salida_cercanos.txt')
        self.assertTrue(filecmp.cmp('cercanos.txt','salida_cercanos.txt'))

####################################################################

unittest.main()
