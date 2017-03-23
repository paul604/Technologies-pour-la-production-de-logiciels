import sqlite3
from ..bean.Activite import Activite

def db2object(project_root, a_id=-1):
    '''
    Retourne l'activite avec l'id passé en param ou si id = -1 retourne l'ensemble des activites contenus dans la base de données sous forme d'objets Activite
    '''

    try:
        conn = sqlite3.connect(project_root+'/data/database/db.db')

        cur = conn.cursor()
        if(a_id == -1):
            cur.execute("""SELECT activites.id, activites.nom, activites.numero_activites ,activites.numero_equipements, activites.desc_act
                FROM activites
                """)
        else:
            cur.execute("""SELECT activites.id, activites.nom, activites.numero_activites ,activites.numero_equipements, activites.desc_act
                FROM activites
                WHERE activites.id=?
            """, (a_id, ))


        rows = cur.fetchall()

        activites = set()

        for row in rows:
            activites.add(Activite(
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

    return activites
