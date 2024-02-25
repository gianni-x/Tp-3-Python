from typing import List,Tuple,Set,TextIO,Dict
from alojamiento_turistico import AlojamientoTuristico
from establecimiento_gastronomico import EstablecimientoGastronomico
import csv

class DataSetTuristico:
    def __init__(self,
                 filename_aloj_turisticos:str,
                 filename_est_gastronomicos:str):
        ''' Inicializa el DataSetTuristico, cargando los datos:
            filename_aloj_turisticos: CSV con los alojamientos turísticos;
            filename_est_gastronomicos: CSV con los establecimientos gastronómicos.
        '''
        self._aloj_turisticos = self._leer_aloj_turisiticos(filename_aloj_turisticos)      # O(A)
        self._aloj_turisticos.sort()                                                       # O(A*log(A))
        self._est_gastronomicos = self._leer_est_gastronomicos(filename_est_gastronomicos) # O(E)

    def _leer_aloj_turisiticos(self, filename:str):
        ''' Devuelve una lista con instancias de AlojamientoTuristico
            consitruidas a partir de la información del CSV filename.'''
        f:TextIO = open(filename)                                      # O(1)
        alojs:List[AlojamientoTuristico] = []                          # O(1)
        linea:Dict[str,str]                                            # O(1)
        for linea in csv.DictReader(f):     # repite A veces operaciones O(1)
            lng_str:str    = linea['Long'].strip()                     # O(1)
            lat_str:str    = linea['Lat'].strip()                      # O(1)
            if lng_str != '' and lat_str != '':                        # O(1)
                lng:float      = float(lng_str)                        # O(1)
                lat:float      = float(lat_str)                        # O(1)
                nom:str        = linea['nombre']                       # O(1)
                calle_nom:str  = linea['calle']                        # O(1)
                calle_alt:int  = int(linea['altura'])                  # O(1)
                tel:str        = linea['telefono']                     # O(1)
                mail:str       = linea['email']                        # O(1)
                aloj:AlojamientoTuristico = AlojamientoTuristico(
                       lng, lat, nom, calle_nom, calle_alt, tel, mail) # O(1)
                alojs.append(aloj)                                     # O(1)
        f.close()                                                      # O(1)

    def _leer_est_gastronomicos(self, filename:str):
        ''' Devuelve una lista con instancias de EstablecimientoGastronomico
            consitruidas a partir de la información del CSV filename.'''
        f:TextIO = open(filename)                                  # O(1)
        ests:List[EstablecimientoGastronomico] = []                # O(1)
        linea:Dict[str,str]                                        # O(1)
        for linea in csv.DictReader(f): # repite E veces operaciones O(1)
            lng_str:str    = linea['long'].strip()                 # O(1)
            lat_str:str    = linea['lat'].strip()                  # O(1)
            if lng_str != '' and lat_str != '':                    # O(1)
                lng:float      = float(linea['long'])              # O(1)
                lat:float      = float(linea['lat'])               # O(1)
                nom:str        = linea['establecimiento']          # O(1)
                rub:str        = linea['rubro']                    # O(1)
                calle_nom:str  = linea['calle']                    # O(1)
                calle_alt:int  = int(linea['altura'])              # O(1)
                est:EstablecimientoGastronomico = EstablecimientoGastronomico(
                      lng, lat, nom, rub, calle_nom, calle_alt)    # O(1)
                ests.append(est)                                   # O(1)
        f.close()                                                  # O(1)
        return ests                                                # O(1)

    def alojamientos(self) -> List[AlojamientoTuristico]:
        ''' Requiere: nada
            Devuelve: un lista con los alojamientos turísticos del dataset
                      ordenados por nombre.
        ''' 
        return self._aloj_turisticos     # O(1)

    def alojamiento_por_nombre(self, nom:str) -> AlojamientoTuristico:
        ''' Requiere: nom es el nombre de un alojamiento existente en el dataset.
            Devuelve: la instancia de AlojamientoTuristico del dataset cuyo
                      nombre es nom.
        '''
        izq:int = 0                                           # O(1)
        der:int = len(self._aloj_turisticos)                  # O(1)
        aloj:AlojamientoTuristico                             # O(1)
        encontrado:bool = False                               # O(1)
        while not encontrado: # repite log(A) veces operaciones O(1)
            med:int = (izq + der) // 2                        # O(1)
            aloj = self._aloj_turisticos[med]                 # O(1)
            if aloj.nombre == nom:                            # O(1)
                encontrado = True                             # O(1)
            elif aloj.nombre < nom:                           # O(1)
                izq = med + 1                                 # O(1)
            else:
                der = med                                     # O(1)
        return aloj                                           # O(1)

    def tres_boliches_cercanos(self, aloj:AlojamientoTuristico) -> \
                                     Tuple[EstablecimientoGastronomico, \
                                     EstablecimientoGastronomico, \
                                     EstablecimientoGastronomico]:
        ''' Requiere: en el dataset hay al menos 3 establecimientos gastronómicos.
            Devuelve: una tupla con los tres establecimientos gastronómicos más
                      próximos a aloj.
        '''
        cercanos:Tuple[EstablecimientoGastronomico, \
                       EstablecimientoGastronomico, \
                       EstablecimientoGastronomico]
        cercanos = self._boliches_ordenados(aloj,                       \
                                       self._est_gastronomicos[0], \
                                       self._est_gastronomicos[1], \
                                       self._est_gastronomicos[2])                      # O(1)
        tercera_dist:long =  aloj.distancia(cercanos[2].latitud, cercanos[2].longitud)  # O(1)
        for eg in self._est_gastronomicos[3:]:          # repite E - 3 veces operaciones  O(E)
            dist = aloj.distancia(eg.latitud, eg.longitud)                              # O(1)
            if dist < tercera_dist:                                                     # O(1)
                cercanos = self._boliches_ordenados(aloj,cercanos[0],cercanos[1],eg)    # O(1)
                tercera_dist = aloj.distancia(cercanos[2].latitud, cercanos[2].longitud)# O(1)
        return cercanos                                                                 # O(1)


    def _boliches_ordenados(self, aloj:AlojamientoTuristico,\
                            e1:EstablecimientoGastronomico, \
                            e2:EstablecimientoGastronomico, \
                            e3:EstablecimientoGastronomico) \
                    -> Tuple[EstablecimientoGastronomico,   \
                             EstablecimientoGastronomico,   \
                             EstablecimientoGastronomico]:
        ''' Devuelve una tupla en la que e1, e2 y e3 aparecen ordenados
            respecto a la distancia a la que se encuentran de aloj.
        '''
        dist1:long = aloj.distancia(e1.latitud, e1.longitud) # O(1)
        dist2:long = aloj.distancia(e2.latitud, e2.longitud) # O(1)
        dist3:long = aloj.distancia(e3.latitud, e3.longitud) # O(1)

        if dist1 <= dist2 and dist2 <= dist3:                  # O(1)
            return (e1,e2,e3)                                # O(1)
        elif dist1 <= dist3 and dist3 <= dist2:                # O(1)
            return (e1,e3,e2)                                # O(1)
        elif dist2 <= dist1 and dist1 <= dist3:                # O(1)
            return (e2,e1,e3)                                # O(1)
        elif dist2 <= dist3 and dist3 <= dist1:                # O(1)
            return (e2,e3,e1)                                # O(1)
        elif dist3 <= dist1 and dist1 <= dist2:                # O(1)
            return (e3,e1,e2)                                # O(1)
        else:
            return (e3,e2,e1)                                # O(1)

    def boliche_proximo_de_rubro(self, aloj:AlojamientoTuristico, rub:str) -> EstablecimientoGastronomico:
        ''' Requiere: en el dataset hay al menos un establecimiento turístico
                      cuyo rubro es rub.
            Devuelve: el establecimiento más próximo a aloj cuyo rubro es rub.
        '''
        est_mas_cercano = None                                               # O(1)
        est_mas_cercano_dist = None                                          # O(1)
        for e in self._est_gastronomicos:         # repite E veces operaciones O(1)
            if e.rubro == rub:                                               # O(1)
                e_dist:long = aloj.distancia(e.latitud, e.longitud)          # O(1)
                if est_mas_cercano is None or e_dist < est_mas_cercano_dist: # O(1)
                    est_mas_cercano = e                                      # O(1)
                    est_mas_cercano_dist = e_dist                            # O(1)
        return est_mas_cercano                                               # O(1)

    def rubros_en_zona(self, aloj:AlojamientoTuristico, dist:int) -> Set[str]:
        ''' Requiere: hay al menos un alojamiento turístico en el dataset y
                      dist >= 0.
            Devuelve: el conjunto de los rubros de los establecimeintos gastronómicos
                      que se encuentran a menos de dist metros de aloj.
        '''
        vr:Set[str] = set()
        for est in self._est_gastronomicos:
            if aloj.distancia(est.latitud, est.longitud) < dist:
                vr.add(est.rubro)
        return vr

    def exportar_cercanos(self, nom_archivo:str):
        '''Requiere: nada.
           Devuelve: nada.
           Modifica: genera un archivo, de nombre nom_archivo, que indica de
                     cada alojmiento turístico cuáles son los tres establecimientos
                     gastronómicos más cercanos. Cada línea del archivo de salida
                     incluye la información correspondiente a un alojamiento
                     turístico y sigue el formato "a -> e1 | e2 | e3", donde a es
                     la representación como str del alojamiento y ei la representación
                     como str del establecimiento i (con 1<=i<=3). En el archivo,
                     los alojamientos aparecen listados alfabéticamente y los
                     establecimientos por próximidad al alojamiento en cuestión.
        '''
        f:TextIO = open(nom_archivo, 'w')
        for aloj in self._aloj_turisticos:
            cercanos:Tuple[EstablecimientoGastronomico, \
                           EstablecimientoGastronomico, \
                           EstablecimientoGastronomico] = self.tres_boliches_cercanos(aloj)
            f.write(str(aloj) + ' -> ' + \
                    str(cercanos[0]) + ' | ' +
                    str(cercanos[1]) + ' | ' +
                    str(cercanos[2]) + '\n' )
        f.close()
