import sqlite3
from config import DB_FULLPATH, printex
from ..bean.Installation import Installation



def i_get_object_by_id(i_id=-1):
    '''
    Retourne un set des instllations existantes en base
    '''
    installations = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        if(i_id == -1): # toutes
            cur.execute("""SELECT i.numero, i.nom, a.adresse, a.code_postal, a.ville FROM installation i, adresse a WHERE i.numero=a.numero""")
        else: # via id
            cur.execute("""SELECT i.numero, i.nom, a.adresse, a.code_postal, a.ville FROM installation i, adresse a WHERE i.numero=a.numero AND i.numero=?""", [i_id])
        rows = cur.fetchall()
        for row in rows:
            installations.add(Installation(row[0], row[1], row[2], row[3], row[4]))
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return installations



def i_get_object_by_ville(ville):
    '''
    Retourne les installations d'une ville donnée
    '''
    installations = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT i.numero, i.nom, a.adresse, a.code_postal, a.ville FROM installation i, adresse a WHERE i.numero=a.numero AND a.ville=?""", [ville])
        rows = cur.fetchall()
        for row in rows:
            installations.add(Installation(row[0], row[1], row[2], row[3], row[4]))
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return installations



def i_get_object_by_cp(code_postal):
    '''
    Retourne les installations correspondant à un code postal donné
    '''
    installations = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT i.numero, i.nom, a.adresse, a.code_postal, a.ville FROM installation AS i, adresse AS a WHERE i.numero=a.numero AND a.code_postal=?""", [code_postal])
        rows = cur.fetchall()
        for row in rows:
            installations.add(Installation(row[0], row[1], row[2], row[3], row[4]))
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return installations