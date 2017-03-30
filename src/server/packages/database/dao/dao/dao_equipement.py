import sqlite3
from config import DB_FULLPATH, printex
from ..bean.Equipement import Equipement
from ..bean.Adresse import Adresse
from ..bean.Activite import Activite



def e_get_object_by_id(e_id = -1):
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
        printex(e)
    finally:
        conn.close()
    return equipements



def e_get_addr_act():
    '''
    Retourne un set comprenant des tuples (Equipement, Adresse, Activite)
    '''
    results = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""
                    SELECT e.numero_equipements, e.nom, e.numero_installation, e.latitude, e.longitude, addr.numero, addr.adresse, addr.code_postal, addr.ville, act.id, act.nom, act.numero_activites, act.numero_equipements, act.desc_act
                    FROM equipement e, adresse addr, activite act
                    WHERE e.numero_installation=addr.numero AND e.numero_equipements=act.numero_equipements
                    """)
        rows = cur.fetchall()
        for row in rows:
            results.add((Equipement(row[0], row[1], row[2], row[3], row[4]), Adresse(row[5], row[6], row[7], row[8]), Activite(row[9], row[10], row[11], row[12], row[13])))
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return results
 