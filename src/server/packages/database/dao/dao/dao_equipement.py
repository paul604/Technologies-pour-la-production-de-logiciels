import sqlite3
from config import DB_FULLPATH
from ..bean.Equipement import Equipement

def e_get_object_by_id(e_id=-1):
    '''
    Retourne l'equipements avec l'id passé en param ou si id == -1 retourne l'ensemble des equipements contenus dans la base de données sous forme d'objets Equipement
    '''

    try:
        conn = sqlite3.connect(DB_FULLPATH)

        cur = conn.cursor()
        if(e_id == -1):
            #get tout les equipements
            cur.execute("""SELECT *
                FROM equipement
                """)
        else:
            #get l'equipements avec l'id
            cur.execute("""SELECT *
                FROM equipement
                WHERE equipement.numero_equipements=?
            """,  (e_id, ))


        rows = cur.fetchall()

        equipements = set()

        # add toute les valeur d'un tuple du select dans un objet Equipement puis on ajoute cette object dans un set.
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
