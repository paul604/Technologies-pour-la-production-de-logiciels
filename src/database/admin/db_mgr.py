
import os
import sqlite3

def create_db():
	'''

	'''
	# on crée le dossier s'il n'existe pas
	if not os.path.exists('data'):
		os.mkdir('data');

	# on crée le dossier s'il n'existe pas
	if not os.path.exists('data/database'):
		os.mkdir('data/database')

	try:
		conn = sqlite3.connect('data/database/db.db')

		cursor = conn.cursor()
		#clé étrangère ??

		#numero== id instal
		cursor.execute("""CREATE TABLE IF NOT EXISTS installation(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	nom TEXT
			)
		""")

		#numero== a numero dans installation
		cursor.execute("""CREATE TABLE IF NOT EXISTS adresse(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	adresse TEXT,
	     	code_postal TEXT,
	     	ville TEXT
			)
		""")

		#numero==EquipementId
		cursor.execute("""CREATE TABLE IF NOT EXISTS equipements(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	nom TEXT,
	     	numero_installation INTEGER,
	     	latitude REAL,
	     	longitude REAL
			)
		""")
		
		cursor.execute("""CREATE TABLE IF NOT EXISTS activites(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	nom TEXT
			)
		""")
		cursor.execute("""CREATE TABLE IF NOT EXISTS equipements_activites(
	    	numero_equipements INTEGER UNIQUE,
	    	numero_activites INTEGER UNIQUE,
			PRIMARY KEY (numero_equipements,  numero_activites)
			)
		""")
		conn.commit()
	except Exception as e:
		print (type(e))
		conn.rollback()
	finally:
		conn.close()

# def csv_to_db():



create_db()
