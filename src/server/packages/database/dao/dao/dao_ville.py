import sqlite3
from config import DB_FULLPATH, printex



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
        printex(e)
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
        printex(e)
    finally:
        conn.close()
    return cps



def cp_and_v_getall():
    '''
    Retourne un set des codes postaux existants en base
    '''
    cp_and_v = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT code_postal,ville FROM adresse""")
        for v in cur.fetchall():
            cp_and_v.add(v)
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return cp_and_v



def cp_getville(cp):
    '''
    Retourne les villes correspondant à un code postal
    '''
    villes = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cur = conn.cursor()
        cur.execute("""SELECT ville FROM adresse AS a WHERE a.code_postal=?""", [cp])
        for v in cur.fetchall():
            villes.add(v)
    except Exception as e:
        printex(e)
    finally:
        conn.close()
    return villes
