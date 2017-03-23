
import csv
import sqlite3

def csv2db_installation(project_root):
    '''
    update de la table installations de la db en utilisant le fichier csv.
    '''

    file = open(project_root+'/data/csv/installations.csv','r')
    read = csv.DictReader(file)
    tab_installation = []
    tab_addr = []
    for row in read:
        # print(row['Nom du lieu dit']+','+row['Numero de la voie']+","+row['Nom de la voie'])
        # break
		#tuple dans tab
        tab_installation.append((row["Numéro de l\'installation"]
            ,row['Nom usuel de l\'installation']
            ));

        tab_addr.append((
            row["Numéro de l\'installation"]
            ,row['Nom du lieu dit']+','+row['Numero de la voie']+","+row['Nom de la voie']
            ,row['Code postal']
            ,row['Nom de la commune']
        ))

    try:
        conn = sqlite3.connect(project_root+'/data/database/db.db')
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM installation;
        """)
        cursor.execute("""
            DELETE FROM adresse;
        """)

        cursor.executemany('INSERT INTO installation VALUES (?,?)', tab_installation)
        cursor.executemany('INSERT INTO adresse VALUES (?,?,?,?)', tab_addr)

        conn.commit()

    except Exception as e:
    	print (type(e))
    	conn.rollback()
    finally:
    	conn.close()
