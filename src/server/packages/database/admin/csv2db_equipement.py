
import csv, sqlite3, os
from config import PROJECT_ROOT, DB_FULLPATH

def csv2db_equipement():
    '''
    update de la table equipements de la db en utilisant le fichier csv.
    '''

    #get le CSV
    file = open(PROJECT_ROOT + os.path.sep + 'data' + os.path.sep + 'csv' + os.path.sep + 'equipements.csv','r')
    read = csv.DictReader(file)

    tab_equipements = []
    # foreach sur le CSV et ajout dans un tableau pour ajout dans bdd
    for row in read:
        tab_equipements.append((
                row['EquipementId']
                ,row['EquNom']
                ,row['InsNumeroInstall']
                ,row['EquGpsY']
                ,row['EquGpsX']
            ));

    try:
        conn = sqlite3.connect(DB_FULLPATH)
        cursor = conn.cursor()

        # DELETE les donnees pour éviter les doublon
        cursor.execute("""
            DELETE FROM equipements;
        """)

        # add les data du tableau tab_equipements dans la bdd 
        cursor.executemany('INSERT INTO equipements VALUES (?,?,?,?,?)', tab_equipements)

        conn.commit()

    except Exception as e:
    	print (type(e))
    	conn.rollback()
    finally:
    	conn.close()
