#!/usr/bin/env python3
# coding=utf8



'''
Contient l'exécution séquentielle des différentes fonctions
Permet de tester le bon enchaînement des différents appels
'''



# évite de générer des dossier __pycache__ indésirables dans l'arborescence du projet
import sys
sys.dont_write_bytecode = True



# autres imports
from packages.database.admin.get_data import dl_data
from packages.database.admin.db_mgr import create_db
from packages.database.admin.csv2db_installation import csv2db_installation
from packages.database.admin.csv2db_equipement import csv2db_equipement
from packages.database.admin.csv2db_activite import csv2db_activite
from packages.rest.api.endpoint import launch_rest_api_service



dl_data()
create_db()
csv2db_installation()
csv2db_equipement()
csv2db_activite()
launch_rest_api_service()

