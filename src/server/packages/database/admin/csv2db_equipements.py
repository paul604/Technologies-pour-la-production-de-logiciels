
import csv
import sqlite3

def csv2db_equipements(project_root):
    '''
    update de la table equipements de la db en utilisant le fichier csv.
    '''

    #get le CSV
    file = open(project_root+'/data/csv/equipements.csv','r')
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
        conn = sqlite3.connect(project_root+'/data/database/db.db')
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
