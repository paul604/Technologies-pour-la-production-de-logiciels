
import csv, sqlite3, os
from config import PROJECT_ROOT, DB_FULLPATH, DB_FULL_NAME, printerr

def csv2db_equipement(update = False):
    '''
    Le paramètre d'override update permet d'activer ou non l'écrasement du contenu actuel de la base de donnée par celui du fichier CSV
    Mettre à True pour mettre-à-jour
    '''

    if update:
        #get le CSV
        file_full_name = 'equipements.csv'
        file_path = PROJECT_ROOT + os.path.sep + 'data' + os.path.sep + 'csv' + os.path.sep + file_full_name
        file = open(file_path,'r')
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

            # DELETE les données afin d'éviter les doublons
            cursor.execute("""DELETE FROM equipement;""")

            # add les data du tableau tab_equipements dans la bdd
            cursor.executemany('INSERT INTO equipement VALUES (?,?,?,?,?)', tab_equipements)

            conn.commit()
            printerr(file_full_name + ' stored successfully into database ' + DB_FULL_NAME)
        except Exception as e:
            conn.rollback()
            printerr(type(e))
            printerr('exception occured while attempted to store ' + file_full_name + ' into database ' + DB_FULL_NAME)
            printerr('==============')
            printerr(e)
        finally:
        	conn.close()
