import sqlite3
from config import DB_FULLPATH



def v_getall():
    '''
    Retourne un set des villes existantes en base
    '''
    villes = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT ville FROM adresse""")
        for v in cur.fetchall():
            villes.add(v)
    except Exception as e:
        print (type(e))
        print("-------------------------")
        print (e)
    finally:
        conn.close()
    return villes



def cp_getall():
    '''
    Retourne un set des codes postaux existants en base
    '''
    cps = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT code_postal FROM adresse""")
        for v in cur.fetchall():
            cps.add(v)
    except Exception as e:
        print (type(e))
        print("-------------------------")
        print (e)
    finally:
        conn.close()
    return cps



def v_and_cp_getall():
    '''
    Retourne un set des codes postaux existants en base
    '''
    v_and_cp = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT ville,code_postal FROM adresse""")
        for v in cur.fetchall():
            v_and_cp.add(v)
    except Exception as e:
        print (type(e))
        print("-------------------------")
        print (e)
    finally:
        conn.close()
    return v_and_cp
