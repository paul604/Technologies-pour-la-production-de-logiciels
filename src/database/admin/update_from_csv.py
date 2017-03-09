
import csv

def csv2db_installation():
    '''
    update de la table installations de la db en utilisant le fichier csv.
    '''

    read = csv.DictReader(file)
    file = open('data/csv/installations.csv','r')
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
    conn = sqlite3.connect('data/database/db.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO installation VALUES (?,?)', tab_instalation)
    cursor.executemany('INSERT INTO adresse VALUES (?,?,?,?)', tab_addr)

up_installations()
