class Installation:
	'''
	Classe représentant une installation.
	'''

	def __init__(self, id, nom, adresse, code_postal, ville):
		self.id = id
		self.nom = nom
		self.adresse = adresse
		self.code_postal = code_postal
		self.ville = ville

	def __repr__(self):
		return str(self.id)+' '+self.nom+' '+self.adresse+' '+str(self.code_postal)+' '+self.ville
