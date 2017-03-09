
import sqlite3

def create_db():
	'''

	'''

	# on crée le dossier s'il n'existe pas
	if not os.path.exists('database'):
		os.mkdir('database')

	try:
		conn = sqlite3.connect('database/db.db')

		cursor = conn.cursor()
		#clé étrangère ??
		cursor.execute("""CREATE TABLE IF NOT EXISTS installation(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	nom TEXT,
	     	adresse TEXT,
	     	code_postal TEXT,
	     	ville TEXT,
	     	latitude REAL,
	     	longitude REAL
			)
		""")
		cursor.execute("""CREATE TABLE IF NOT EXISTS equipements(
	    	numero INTEGER PRIMARY KEY UNIQUE,
	     	nom TEXT,
	     	numero_installation INTERGER,
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

def up_t_installations():

	read = csv.reader(open("data/installations.csv","rb"))
	for row in read:
		print(row)
		#tuple dans tab
