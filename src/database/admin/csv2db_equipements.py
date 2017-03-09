
import csv
import sqlite3

def csv2db_equipements():
    '''
    update de la table equipements de la db en utilisant le fichier csv.
    '''

    file = open('data/csv/equipements.csv','r')
    read = csv.DictReader(file)
    tab_equipements = []
    for row in read:
        # print(row['Nom du lieu dit']+','+row['Numero de la voie']+","+row['Nom de la voie'])
        # break
		#tuple dans tab
        tab_instalation.append((
                row['InsNumeroInstall']
                ,row['EquNom']
                ,row['InsNumeroInstall']
                ,row['EquGpsY']
                ,row['EquGpsX']
            ));

    try:
        conn = sqlite3.connect('data/database/db.db')
        cursor = conn.cursor()

        cursor.executemany('INSERT INTO equipements VALUES (?,?,?,?,?)', tab_instalation)

        conn.commit()

    except Exception as e:
    	print (type(e))
    	conn.rollback()
    finally:
    	conn.close()


#test

csv2db_equipements()

try:
    conn2 = sqlite3.connect('data/database/db.db')
    cursor2 = conn2.cursor()
    for row in cursor2.execute('SELECT * FROM equipements',):
        print (row)

except Exception as e:
    raise
finally:
    conn2.close()
