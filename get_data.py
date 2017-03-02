#!/usr/bin/env python3.4

'''
Fournit un ensemble de fonction pour :
	* télécharger les fichiers CSV contenant les données
	* les parser pour en insérer les données dans une base SQLite
'''

import os, urllib.request
import sqlite3

def dl_data(override = False):
	'''
	Le paramètre override permet d'activer ou non l'écrasement des CSV.
	Activer pour les télécharger à nouveau les CVS même si les fichiers existent.
	'''

	# on crée le dossier s'il n'existe pas
	if not os.path.exists('data'):
		os.mkdir('data');

	# on y télécharge les CSV
	if override or not os.path.isfile('data/installations.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=csv', 'data/installations.csv')
	if override or not os.path.isfile('data/equipements.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/fileadmin/data/datastore/rpdl/sport/23440003400026_J336/equipements.csv', 'data/equipements.csv')
	if override or not os.path.isfile('data/activites.csv'):
		urllib.request.urlretrieve('http://data.paysdelaloire.fr/fileadmin/data/datastore/pdl/PLUS15000/J334_equipements_activites.csv', 'data/activites.csv')


def create_db():
	'''

	'''

	# on crée le dossier s'il n'existe pas
	if not os.path.exists('database'):
		os.mkdir('database')

	try:
		conn = sqlite3.connect('db.db')

		cursor = conn.cursor()
		#clé étrangère ??
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS installation(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	nom TEXT,
	     	adresse TEXT,
	     	code_postal TEXT,
	     	ville TEXT,
	     	age REAL
	     	age REAL
			)
			""")
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS equipements(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	nom TEXT,
	     	numero_installation INTERGER
			)
			""")
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS activites(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	nom TEXT
			)
			""")
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS equipements_activites(
	    	numero_equipements INTEGER PRIMARY KEY UNIQUE,
	    	numero_activites INTEGER PRIMARY KEY UNIQUE
			)
			""")
		conn.commit()
	except Exception as e:
    	print("Erreur")
    	conn.rollback()
	finally:
		db.close()
