#!/usr/bin/env python3.4


'''
Contient l'exécution séquentielle des différentes fonctions.
Permet de tester le bon enchaînement des différents appels.
'''


# évite de générer des dossier __pycache__ indésirables dans l'arborescence du projet
import sys
sys.dont_write_bytecode = True


# on récupère le path de la racine du projet en sachant que le main est toujours placé à la racine du projet sous src
# <project_root>/src/main.py
import os
project_root = os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/../..')


# autres imports
from database.admin.get_data import dl_data
from database.admin.db_mgr import create_db
from database.admin.csv2db_installation import csv2db_installation
from rest.api.endpoint import launch_rest_api_service


dl_data(project_root)
create_db(project_root)
csv2db_installation(project_root)
launch_rest_api_service()


