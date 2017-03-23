import sqlite3
from ..bean.Installation import Installation

def db2object(project_root, id=-1):
    '''
    Retourne l'ensemble des installations contenus dans la base de données sous forme d'objets Installation
    '''

    try:
        conn = sqlite3.connect(project_root+'/data/database/db.db')

        cur = conn.cursor()
        if(id == -1):
            cur.execute("""SELECT installation.numero, installation.nom, adresse.adresse, adresse.code_postal, adresse.ville
                FROM installation, adresse
                WHERE installation.numero=adresse.numero
            """)
        else:
            cur.execute("""SELECT installation.numero, installation.nom, adresse.adresse, adresse.code_postal, adresse.ville
                FROM installation, adresse
                WHERE installation.numero=adresse.numero, installation.numero=?
            """, id)

        rows = cur.fetchall()

        installations = set()

        for row in rows:
            installations.add(Installation(
                row[0]
                ,row[1]
                ,row[2]
                ,row[3]
                ,row[4]
            ))

    except Exception as e:
        print (type(e))
        print("-------------------------")
        print (e)

    finally:
        conn.close()

    return installations
