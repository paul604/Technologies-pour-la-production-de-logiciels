
import csv, sqlite3, os
from config import PROJECT_ROOT, DB_FULLPATH

def csv2db_installation():
    '''
    update de la table installations de la db en utilisant le fichier csv.
    '''

    #get le CSV
    file = open(PROJECT_ROOT + os.path.sep + 'data' + os.path.sep + 'csv' + os.path.sep + 'installations.csv','r')
    read = csv.DictReader(file)

    tab_installation = []
    tab_addr = []

    # foreach sur le CSV et ajout dans un tableau pour ajout dans bdd
    for row in read:
        tab_installation.append((row["Numéro de l\'installation"]
            ,row['Nom usuel de l\'installation']
            ));

        tab_addr.append((
            row["Numéro de l\'installation"]
            ,row['Nom du lieu dit']+','+row['Numero de la voie']+','+row['Nom de la voie']
            ,row['Code postal']
            ,row['Nom de la commune']
        ))

    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cursor = conn.cursor()

        # DELETE les donnees pour éviter les doublon
        cursor.execute("""
            DELETE FROM installation;
        """)
        cursor.execute("""
            DELETE FROM adresse;
        """)

        # add les data du tableau tab_installation et tab_addr dans la bdd 
        cursor.executemany('INSERT INTO installation VALUES (?,?)', tab_installation)
        cursor.executemany('INSERT INTO adresse VALUES (?,?,?,?)', tab_addr)

        conn.commit()

    except Exception as e:
    	print (type(e))
    	conn.rollback()
    finally:
    	conn.close()
