#!/usr/bin/env python3
# coding=utf8

'''
Contient l'exécution séquentielle des différentes fonctions.
Permet de tester le bon enchaînement des différents appels.
'''


# évite de générer des dossier __pycache__ indésirables dans l'arborescence du projet
import sys
sys.dont_write_bytecode = True


# on récupère le path de la racine du projet en sachant que le main est toujours placé à la racine du projet sous src/server
# <project_root>/src/main.py
import os
project_root = os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/../..')




# autres imports
from packages.database.admin.get_data import dl_data
from packages.database.admin.db_mgr import create_db
from packages.database.admin.csv2db_installation import csv2db_installation
from packages.rest.api.endpoint import launch_rest_api_service
from packages.database.dao.dao.dao_installation import *


dl_data(project_root)
create_db(project_root)
csv2db_installation(project_root)
db2object(project_root, 440370001)
launch_rest_api_service()
