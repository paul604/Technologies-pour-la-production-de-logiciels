

'''
Télécharge les données sous forme de fichiers CSV
'''

import os, urllib.request, csv
from config import PROJECT_ROOT

def dl_data(override = False):
	'''
	Le paramètre override permet d'activer ou non l'écrasement des CSV.
	Activer pour les télécharger à nouveau les CSV même si les fichiers existent.
	'''

	# on crée le dossier s'il n'existe pas
	if not os.path.exists(PROJECT_ROOT+'/data'):
		os.mkdir(PROJECT_ROOT+'/data');

	if not os.path.exists(PROJECT_ROOT+'/data/csv'):
		os.mkdir(PROJECT_ROOT+'/data/csv');

	# on y télécharge les CSV
	if override or not os.path.isfile(PROJECT_ROOT+'/data/csv/installations.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=csv', PROJECT_ROOT+'/data/csv/installations.csv')
	if override or not os.path.isfile(PROJECT_ROOT+'/data/csv/equipements.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/fileadmin/data/datastore/rpdl/sport/23440003400026_J336/equipements.csv', PROJECT_ROOT+'/data/csv/equipements.csv')
	if override or not os.path.isfile(PROJECT_ROOT+'/data/csv/activites.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/fileadmin/data/datastore/pdl/PLUS15000/J334_equipements_activites.csv', PROJECT_ROOT+'/data/csv/activites.csv')
