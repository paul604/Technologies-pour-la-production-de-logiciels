

'''
Télécharge les données sous forme de fichiers CSV via le site opendata PDLL
'''

import os, urllib.request, csv
from config import PROJECT_ROOT, printerr

def dl_data(override = False):
	'''
	Le paramètre override permet d'activer ou non l'écrasement des CSV
	Activer pour les télécharger à nouveau les CSV même si les fichiers existent
	'''

	path1 = PROJECT_ROOT + os.path.sep + 'data'
	path2 = path1 + os.path.sep + 'csv'
	
	i_path = path2 + os.path.sep + 'installations.csv'
	i_url = 'http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=csv'
	
	e_path = path2 + os.path.sep + 'equipements.csv'
	e_url = 'http://data.paysdelaloire.fr/fileadmin/data/datastore/rpdl/sport/23440003400026_J336/equipements.csv'

	a_path = path2 + os.path.sep + 'activites.csv'
	a_url = 'http://data.paysdelaloire.fr/fileadmin/data/datastore/pdl/PLUS15000/J334_equipements_activites.csv'



	# ----------------- on crée l'arborescence si elle n'existe pas
	if not os.path.exists(path1):
		os.mkdir(path1);
		printerr('directory created : "' + path1 + '"')

	if not os.path.exists(path2):
		os.mkdir(path2);
		printerr('directory created : "' + path2 + '"')

	# ----------------- on y télécharge les fichiers CSV s'ils ny sont pas présents ou que l'écrasement a été spécifié
	if override or not os.path.isfile(i_path):
		printerr('fetching "installations" data at "' + i_url + '"')
		urllib.request.urlretrieve(i_url, i_path)
		printerr('file "installations.csv" created at "' + i_path + '"')

	if override or not os.path.isfile(e_path):
		printerr('fetching "equipements" data at "' + e_url + '"')
		urllib.request.urlretrieve(e_url, e_path)
		printerr('file "equipements.csv" created at "' + e_path + '"')
	
	if override or not os.path.isfile(a_path):
		printerr('fetching "activites" data at "' + a_url + '"')
		urllib.request.urlretrieve(a_url, a_path)
		printerr('file "activites.csv" created at "' + a_path + '"')
