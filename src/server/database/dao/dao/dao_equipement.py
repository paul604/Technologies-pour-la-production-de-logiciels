import sqlite3
from ..bean.Equipement import Equipement

def db2object(project_root, e_id=-1):
    '''
    Retourne l'equipements avec l'id passé en param ou si id = -1 retourne l'ensemble des equipements contenus dans la base de données sous forme d'objets Equipement
    '''

    try:
        conn = sqlite3.connect(project_root+'/data/database/db.db')

        cur = conn.cursor()
        if(e_id == -1):
            cur.execute("""SELECT *
                FROM equipements
                """)
        else:
            cur.execute("""SELECT *
                FROM equipements
                WHERE equipements.numero_equipements=?
            """,  (e_id, ))


        rows = cur.fetchall()

        equipements = set()

        for row in rows:
            equipements.add(Equipement(
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

    return equipements
