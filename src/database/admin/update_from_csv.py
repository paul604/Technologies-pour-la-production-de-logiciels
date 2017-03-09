
import csv
import sqlite3

def csv2db_installation():
    '''
    update de la table installations de la db en utilisant le fichier csv.
    '''

    file = open('data/csv/installations.csv','r')
    read = csv.DictReader(file)
    tab_instalation = []
    tab_addr = []
    for row in read:
        # print(row['Nom du lieu dit']+','+row['Numero de la voie']+","+row['Nom de la voie'])
        # break
		#tuple dans tab
        tab_instalation.append((row["Numéro de l\'installation"]
            ,row['Nom usuel de l\'installation']
            ));

        tab_addr.append((
            row["Numéro de l\'installation"]
            ,row['Nom du lieu dit']+','+row['Numero de la voie']+","+row['Nom de la voie']
            ,row['Code postal']
            ,row['Nom de la commune']
        ))

    try:
        conn = sqlite3.connect('data/database/db.db')
        cursor = conn.cursor()

        cursor.executemany('INSERT INTO installation VALUES (?,?)', tab_instalation)
        cursor.executemany('INSERT INTO adresse VALUES (?,?,?,?)', tab_addr)

        conn.commit()

    except Exception as e:
    	print (type(e))
    	conn.rollback()
    finally:
    	conn.close()


#test

csv2db_installation()

try:
    conn2 = sqlite3.connect('data/database/db.db')
    cursor2 = conn2.cursor()
    for row in cursor2.execute('SELECT * FROM installation',):
        print (row)

except Exception as e:
    raise
finally:
    conn2.close()
