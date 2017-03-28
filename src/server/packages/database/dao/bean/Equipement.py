class Equipement:
	'''
	Classe représentant un équipement.
	'''

	def __init__(self, e_id, nom, numero_installation, latitude, longitude):
		self.id = e_id
		self.nom = nom
		self.numero_installation = numero_installation
		self.latitude = latitude
		self.longitude = longitude

	def __repr__(self):
		return str(self.id)+' '+self.nom+' '+str(self.numero_installation)+' '+str(self.latitude)+' '+str(self.longitude)
