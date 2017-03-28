import sqlite3
from config import DB_FULLPATH
from ..bean.Equipement import Equipement

def e_get_object_by_id(e_id=-1):
    '''
    Retourne un set des équipements existants en base
    '''
    equipements = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        if(e_id == -1): # tous
            cur.execute("""SELECT * FROM equipement""")
        else: # via id
            cur.execute("""SELECT * FROM equipement e WHERE e.numero_equipements=?""",  [e_id])
        rows = cur.fetchall()
        for row in rows:
            equipements.add(Equipement(row[0], row[1], row[2], row[3], row[4]))
    except Exception as e:
        print (type(e))
        print("-------------------------")
        print (e)
    finally:
        conn.close()
    return equipements
