import sqlite3
from ..bean.Installation import Installation

def db2object(project_root):
	'''
	Retourne l'ensemble des installations contenus dans la base de données sous forme d'objets Installation
	'''

	try:
    	conn = sqlite3.connect(project_root+'/data/database/db.db')
    	cur = conn.cursor()
    	cur.execute("""SELECT *
        FROM installation, adresse
        WHERE installation.numero=adresse.numero
    	"""")
    	rows = cur.fetchall()

    	installations = set()

    	for row in rows:
        	installations.add(Installation(
        		row['numero']
        		,row['nom']
        		,row['adresse']
        		,row['code_postal']
        		,row['ville']
        	))

    except Exception as e:
    	print(type(e))

	finally:
    	conn.close()

	return installations
