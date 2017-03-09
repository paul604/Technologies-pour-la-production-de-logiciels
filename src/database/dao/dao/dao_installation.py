import sqlite3

def db2object():
	'''
	Retourne l'ensemble des installations contenus dans la base de données sous forme d'objets <Installations>
	'''

	try:
		conn = sqlite3.connect('data/database/db.db')
		cur = conn.cursor()
		cur.execute("SELECT * FROM installation")
		rows = cur.fetchall()

		for row in rows:
			print(row)

		data = set() # set de retour

	except Exception as e:
		print(type(e))

	finally:
		conn.close()

	return data
