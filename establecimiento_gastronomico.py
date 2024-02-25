class EstablecimientoGastronomico:

	def __init__(self, lng:float, lat:float, nom:str,
		          rub:str, calle_nom:str, calle_alt:int):
		''' Inicializa el EstablecimientoGastronomico con los valores dados. '''
		self.longitud:float   = lng
		self.latitud:float    = lat
		self.nombre:str       = nom
		self.rubro:str        = rub
		self.calle_nombre:str = calle_nom
		self.calle_altura:int = calle_alt

	def __repr__(self) -> str:
		''' Requiere: nada
			Devuelve: Una representación str del EstablecimientoGastronomico.
		'''
		return self.nombre + "@" + self.calle_nombre + ' ' + str(self.calle_altura)

	def __eq__(self, other) -> bool:
		''' Requiere: nada
		    Devuelve: True si todos los campos de self y other son iguales;
			          False en caso contrario.
		'''
		return self.longitud == other.longitud and \
		       self.latitud == other.latitud and \
			   self.nombre == other.nombre and \
			   self.rubro == other.rubro and \
			   self.calle_nombre == other.calle_nombre and \
			   self.calle_altura == other.calle_altura
