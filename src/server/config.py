

'''
from config import PROJECT_ROOT			---> permet de récupérer aisément la racine du projet n'importe où dans /src/server/packages

/!\ L'emplacement de config.py ne doit pas être modifiée sans effectuer les changements adéquats. /!\
C'est lui qui permet de récupérer le chemin absolu de la racine du projet.
'''



import os, sys



# où est-on ?
path_of_here = os.path.abspath(__file__)

# créer la constante
PROJECT_ROOT = os.path.abspath(os.path.dirname(path_of_here)+'/../..')

 # rendre accessible
sys.path.append(path_of_here)
