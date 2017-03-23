class Activite:
	'''
	Classe représentant une activité.
	'''

	def __init__(self, id, nom, numero_activites, numero_equipements, desc_act):
		self.id = id
		self.nom = nom
		self.numero_activites =numero_activites
		self.numero_equipements  =numero_equipements
		self.desc_act =desc_act

	def __repr__(self):
		return str(self.id)+' '+self.nom+' '+str(self.numero_activites)+' '+str(self.numero_equipements)+' '+self.desc_act
