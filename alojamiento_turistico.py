from haversine import haversine,Unit

NO_DISPONIBLE:str = 'N/D'

class AlojamientoTuristico:

	def __init__(self, lng:float, lat:float, nom:str, calle_nom:str,
                      calle_alt:int, tel:str, e_mail:str):
		''' Inicializa el AlojamientoTuristico con los valores dados.'''
		self.longitud:float   = lng
		self.latitud:float    = lat
		self.nombre:str       = nom.upper()
		self.calle_nombre:str = calle_nom
		self.calle_altura:int = calle_alt
		self.telefono:str
		if tel.strip() != '':
			self.telefono  = tel
		else:
			self.telefono  = NO_DISPONIBLE
		self.email:str
		if e_mail.strip() != '':
			self.email = e_mail
		else:
			self.email = NO_DISPONIBLE

	def contacto(self):
		''' Requiere: nada
			Devuelve: si se conoce el telefono y el email del AlojamientoTuristico,
			          la concatenación de los valores de los atributos telefono
			          y email, respetando el siguiente formato: 'telefono | email';
			          si solo se conoce uno de esos atributos, el valor de dicho
			          atributo; si no se conoce ninguno de los dos, 'N/D'.
		'''
		if self.telefono != NO_DISPONIBLE and self.email != NO_DISPONIBLE:
			return self.telefono + ' | ' + self.email
		elif self.telefono != NO_DISPONIBLE:
			return self.telefono
		elif self.email != NO_DISPONIBLE:
			return self.email
		else:
			return NO_DISPONIBLE


	def distancia(self, latitud:float, longitud:float) -> float:
		''' Requiere: nada.
			Devuelve: la distancia en metros entre <latitud,longitud> de este
				      AlojamientoTuristico y el punto <latitud,longitud> dado.
		'''
		return haversine((self.latitud, self.longitud),
				          (latitud, longitud),
				          unit=Unit.METERS)

	def __repr__(self) -> str:
		''' Requiere: nada.
			Devuelve: una representación str del AlojamientoTuristico.
		'''
		return "ALOJAMIENTO:" + str(self.nombre)

	def __lt__(self, other) -> bool:
		''' Requiere: nada
		    Devuelve: True si el nombre de self es menor que el de other
			          de acuerdo al orden lexicográfico; False en caso contrario.
        '''
		return self.nombre < other.nombre

	def __eq__(self, other) -> bool:
		''' Requiere: nada
		    Devuelve: True si todos los campos de self y other son iguales;
			          False en caso contrario.
		'''
		return self.longitud == other.longitud and \
		       self.latitud == other.latitud and \
			   self.nombre == other.nombre and \
			   self.calle_nombre == other.calle_nombre and \
			   self.calle_altura == other.calle_altura and \
			   self.telefono == other.telefono and \
			   self.email == other.email
