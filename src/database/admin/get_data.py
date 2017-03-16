

'''
Fournit un ensemble de fonction pour :
	* télécharger les fichiers CSV contenant les données
	* les parser pour en insérer les données dans une base SQLite
'''

import os, urllib.request
import csv

def dl_data(project_root, override = False):
	'''
	Le paramètre override permet d'activer ou non l'écrasement des CSV.
	Activer pour les télécharger à nouveau les CVS même si les fichiers existent.
	'''

	# on crée le dossier s'il n'existe pas
	if not os.path.exists(project_root+'/data'):
		os.mkdir(project_root+'/data');

	if not os.path.exists(project_root+'/data/csv'):
		os.mkdir(project_root+'/data/csv');

	# on y télécharge les CSV
	if override or not os.path.isfile(project_root+'/data/csv/installations.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=csv', project_root+'/data/csv/installations.csv')
	if override or not os.path.isfile(project_root+'/data/csv/equipements.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/fileadmin/data/datastore/rpdl/sport/23440003400026_J336/equipements.csv', project_root+'/data/csv/equipements.csv')
	if override or not os.path.isfile(project_root+'/data/csv/activites.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/fileadmin/data/datastore/pdl/PLUS15000/J334_equipements_activites.csv', project_root+'/data/csv/activites.csv')
