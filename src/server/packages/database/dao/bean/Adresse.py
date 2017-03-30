class Adresse:
	'''
	Classe représentant une adresse
	'''

	def __init__(self, numero, adresse, code_postal, ville):
		self.numero = numero 
		self.adresse = adresse 
		self.code_postal = code_postal
		self.ville = ville

	def __repr__(self):
		return str(self.numero)+' '+self.adresse+' '+str(self.code_postal)+' '+self.ville
