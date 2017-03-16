
import os
import sqlite3

def create_db():
    '''

    '''
    # on crée le dossier s'il n'existe pas
    if not os.path.exists('data'):
        os.mkdir('data');

    # on crée le dossier s'il n'existe pas
    if not os.path.exists('data/database'):
        os.mkdir('data/database')

    try:
        conn = sqlite3.connect('data/database/db.db')

        cursor = conn.cursor()
        #clé étrangère ??

        #numero== id instal
        cursor.execute("""CREATE TABLE IF NOT EXISTS installation(
            numero INTEGER PRIMARY KEY UNIQUE,
            nom TEXT
            )
        """)

        #numero == a numero dans installation
        cursor.execute("""CREATE TABLE IF NOT EXISTS adresse(
            numero INTEGER PRIMARY KEY UNIQUE,
            adresse TEXT,
            code_postal TEXT,
            ville TEXT,
            FOREIGN KEY (numero) REFERENCES installation(numero)
            )
        """)

        #numero==EquipementId
        cursor.execute("""CREATE TABLE IF NOT EXISTS equipements(
            numero_equipements INTEGER PRIMARY KEY UNIQUE,
            nom TEXT,
            numero_installation INTEGER,
            latitude REAL,
            longitude REAL,
            FOREIGN KEY (numero_installation) REFERENCES installation(numero)
            )
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS activites(
            id INTEGER PRIMARY KEY,
            numero_activites INTEGER,
            numero_equipements INTEGER,
            desc_act TEXT,
            nom TEXT,
            FOREIGN KEY (numero_equipements) REFERENCES equipements(numero_equipements)
            )
        """)

        conn.commit()
    except Exception as e:
        print (type(e))
        print("-------------------------")
        print (e)
        conn.rollback()
    finally:
        conn.close()

def clear_db():
    '''
        permet de clear la db
    '''

    try:
        conn = sqlite3.connect('data/database/db.db')

        cursor = conn.cursor()
        cursor.execute("""
            DROP TABLE IF EXISTS installation;
        """)
        cursor.execute("""
            DROP TABLE IF EXISTS adresse;
        """)
        cursor.execute("""
            DROP TABLE IF EXISTS equipements;
        """)
        cursor.execute("""
            DROP TABLE IF EXISTS activites;
        """)
        conn.commit()
    except Exception as e:
        print (type(e))
        conn.rollback()
    finally:
        conn.close()
