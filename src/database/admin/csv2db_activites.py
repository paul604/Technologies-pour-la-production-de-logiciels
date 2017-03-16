
import csv
import sqlite3

def csv2db_activites():
    '''
    update de la table activites de la db en utilisant le fichier csv.
    '''

    file = open('data/csv/activites.csv','r')
    read = csv.DictReader(file)
    tab_activites = []
    for row in read:
        tab_activites.append((row["ActCode"]
            ,row['EquipementId']
            ,row['ActNivLib']
            ,row['ActLib']
            ));

    try:
        conn = sqlite3.connect('data/database/db.db')
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM activites;
        """)

        cursor.executemany('INSERT INTO activites(numero_activites, numero_equipements, desc_act, nom) VALUES (?,?,?,?)', tab_activites)

        conn.commit()

    except Exception as e:
        print (type(e))
        # print("-------------------------")
        # print (e.arg)
        print("-------------------------")
        print (e)
        conn.rollback()
    finally:
        conn.close()
