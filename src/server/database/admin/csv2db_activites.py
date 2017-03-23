
import csv
import sqlite3

def csv2db_activites(project_root):
    '''
    Mise-à-jour de la table activitées de la base de données en utilisant le fichier csv activites
    '''

    #get le CSV
    file = open(project_root+'/data/csv/activites.csv','r')
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
        conn = sqlite3.connect(project_root+'/data/database/db.db')
        cursor = conn.cursor()

        # DELETE les donnees pour éviter les doublon
        cursor.execute("""
            DELETE FROM activites;
        """)

        # add les data du tableau tab_activites dans la bdd 
        cursor.executemany('INSERT INTO activites(numero_activites, numero_equipements, desc_act, nom) VALUES (?,?,?,?)', tab_activites)

        conn.commit()

    except Exception as e:
        print (type(e))
        print("-------------------------")
        print (e)
        conn.rollback()
    finally:
        conn.close()
