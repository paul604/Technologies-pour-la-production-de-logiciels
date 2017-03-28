import sqlite3
from config import DB_FULLPATH
from ..bean.Activite import Activite



def a_get_object_by_id(a_id = -1):
    
    '''
    Retourne l'activite avec l'id passé en param ou si id == -1 retourne l'ensemble des activites contenus dans la base de données sous forme d'objets Activite
    '''

    activites = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()

        if(a_id == -1):
            #get toute les activites
            cur.execute("""SELECT activite.id, activite.nom, activite.numero_activites ,activite.numero_equipements, activite.desc_act
                FROM activite
                """)
        else:
            #get l'activites avec l'id
            cur.execute("""SELECT activite.id, activite.nom, activite.numero_activites ,activite.numero_equipements, activite.desc_act
                FROM activite
                WHERE activite.id=?
            """, (a_id, ))

        rows = cur.fetchall()
        # add toute les valeur d'un tuple du select dans un objet Activite puis on ajoute cette object dans un set.
        for row in rows:
            activites.add(Activite(
                row[0]
                ,row[1]
                ,row[2]
                ,row[3]
                ,row[4]
            ))
    except Exception as e:
        printerr(type(e))
        printerr("--------------")
        printerr(e)
    finally:
        conn.close()

    return activites
