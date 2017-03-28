import os, sys


'''
from config import PROJECT_ROOT			---> permet de récupérer aisément la racine du projet de n'importe où dans /src/server/packages

/!\ L'emplacement de config.py ne doit pas être modifiée sans effectuer les changements adéquats. /!\
C'est lui qui permet de récupérer le chemin absolu de la racine du projet.
'''
path_of_here = os.path.abspath(__file__)
PROJECT_ROOT = os.path.normpath(os.path.join(os.path.sep, os.path.dirname(path_of_here), '..', '..'))
sys.path.append(path_of_here) # rendre accessible



'''
Définition de constantes pour la base de données, notamment   `DB_FULLPATH`   sera utilisée pour s'y connecter de manière plus souple
'''
DB_FILE_NAME = 'db'
DB_FILE_EXTENSION = 'db'
DB_FULL_NAME = DB_FILE_NAME + '.' + DB_FILE_EXTENSION
DB_DIR = PROJECT_ROOT + os.path.sep + 'data' + os.path.sep + 'database'
DB_FULLPATH = DB_DIR + os.path.sep + DB_FULL_NAME



'''
Définition de méthodes utilitaires globales
'''
def printerr(message):
	sys.stderr.write(message+'\n')
