
import csv, sqlite3, os
from config import PROJECT_ROOT, DB_FULLPATH, DB_FULL_NAME, printerr

def csv2db_installation(update = False):
    '''
    Le paramètre d'override update permet d'activer ou non l'écrasement du contenu actuel de la base de donnée par celui du fichier CSV
    Mettre à True pour mettre-à-jour
    '''

    if update:
        #get le CSV
        file_full_name = 'installations.csv'
        file_path = PROJECT_ROOT + os.path.sep + 'data' + os.path.sep + 'csv' + os.path.sep + file_full_name
        file = open(file_path,'r')
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
            printerr(file_full_name + ' stored successfully into database ' + DB_FULL_NAME)
        except Exception as e:
            conn.rollback()
            printerr(type(e))
            printerr('exception occured while attempted to store ' + file_full_name + ' into database ' + DB_FULL_NAME)
            printerr('==============')
        finally:
        	conn.close()
