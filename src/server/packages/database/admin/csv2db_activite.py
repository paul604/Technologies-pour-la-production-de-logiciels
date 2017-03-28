
import csv, sqlite3, os, sys
from config import PROJECT_ROOT, DB_FULLPATH, DB_FULL_NAME, printerr

def csv2db_activite(update):
    '''
    Le paramètre d'override update permet d'activer ou non l'écrasement du contenu actuel de la base de donnée par celui du fichier CSV
    Mettre à True pour mettre-à-jour
    '''

    if update:
        #get le CSV
        file_full_name = 'activites.csv'
        file_path = PROJECT_ROOT + os.path.sep + 'data' + os.path.sep + 'csv' + os.path.sep + file_full_name
        file = open(file_path,'r')
        read = csv.DictReader(file)

        tab_activites = []
        # foreach sur le CSV et ajout dans un tableau pour ajout dans bdd
        for row in read:
            tab_activites.append((row["ActCode"]
                ,row['EquipementId']
                ,row['ActNivLib']
                ,row['ActLib']
                ));

        try:
            conn = sqlite3.connect(DB_FULLPATH)
            cursor = conn.cursor()

            # DELETE les donnees pour éviter les doublon
            cursor.execute("""DELETE FROM activite;""")

            # add les data du tableau tab_activites dans la bdd 
            cursor.executemany('INSERT INTO activite(numero_activites, numero_equipements, desc_act, nom) VALUES (?,?,?,?)', tab_activites)
            conn.commit()
            printerr(file_full_name + ' dumped successfully into database ' + DB_FULL_NAME + ' (feel free to set `BOOL_IMPORT_CSV_ON_LAUNCH` to `False` in "src/server/config.py" to disable this behaviour)')
        except Exception as e:
            conn.rollback()
            printerr(type(e))
            printerr('exception occured while attempted to store ' + file_full_name + ' into database ' + DB_FULL_NAME)
            printerr('==============')
            printerr(e)
        finally:
            conn.close()
