import sqlite3
from config import DB_FULLPATH
from ..bean.Installation import Installation





def i_get_object_by_id(i_id=-1):
    '''
    Retourne l'installation avec l'id ou si id==-1 retourne l'ensemble des installations contenus dans la base de données sous forme d'objets Installation
    '''

    try:
        conn = sqlite3.connect(DB_FULLPATH)

        cur = conn.cursor()

        if(i_id == -1):
            #get toute les installations
            cur.execute("""SELECT installation.numero, installation.nom, adresse.adresse, adresse.code_postal, adresse.ville
                FROM installation, adresse
                WHERE installation.numero=adresse.numero
            """)
        else:
            #get l'installation avec l'id
            cur.execute("""SELECT installation.numero, installation.nom, adresse.adresse, adresse.code_postal, adresse.ville
                FROM installation, adresse
                WHERE installation.numero=adresse.numero AND installation.numero=?
            """, (i_id, ))

        rows = cur.fetchall()

        installations = set()

        # add toute les valeur d'un tuple du select dans un objet Installation puis on ajoute cette object dans un set.
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






def i_get_object_by_ville(ville):
    '''
    Retourne les installations d'une ville donnée
    '''

    installations = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)

        cur = conn.cursor()


        #get l'installation avec l'id
        cur.execute("""SELECT installation.numero, installation.nom, adresse.adresse, adresse.code_postal, adresse.ville
            FROM installation, adresse
            WHERE installation.numero=adresse.numero AND adresse.ville=?
        """, (ville, ))

        rows = cur.fetchall()

        # add toute les valeur d'un tuple du select dans un objet Installation puis on ajoute cette object dans un set.
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





def i_get_object_by_cp(code_postal):
    '''
    Retourne les installations correspondant à un code postal donné
    '''

    installations = set()
    try:
        conn = sqlite3.connect(DB_FULLPATH)

        cur = conn.cursor()


        #get l'installation avec l'id
        cur.execute("""SELECT installation.numero, installation.nom, adresse.adresse, adresse.code_postal, adresse.ville
            FROM installation, adresse
            WHERE installation.numero=adresse.numero AND adresse.code_postal=?
        """, (code_postal, ))

        rows = cur.fetchall()

        # add toute les valeur d'un tuple du select dans un objet Installation puis on ajoute cette object dans un set.
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