import os, sqlite3
from config import PROJECT_ROOT, DB_DIR, DB_FULLPATH, printerr



def create_db():
    '''
	Crée la base de données
    '''
    if not os.path.exists(DB_FULLPATH):
        path1 = PROJECT_ROOT + os.path.sep + 'data'

        # on crée le dossier s'il n'existe pas
        if not os.path.exists(path1):
            os.mkdir(path1);
            printerr('directory created : "' + path1 + '"')

        # on crée le dossier s'il n'existe pas
        if not os.path.exists(DB_DIR):
            os.mkdir(DB_DIR)
            printerr('directory created : "' + path1 + '"')

        try:
            printerr('starting database creation')
            conn = sqlite3.connect(DB_FULLPATH)
            cursor = conn.cursor()

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
                code_postal INTEGER,
                ville TEXT,
                FOREIGN KEY (numero) REFERENCES installation(numero)
                )
            """)

            #numero_equipements==EquipementId
            cursor.execute("""CREATE TABLE IF NOT EXISTS equipement(
                numero_equipements INTEGER PRIMARY KEY UNIQUE,
                nom TEXT,
                numero_installation INTEGER,
                latitude REAL,
                longitude REAL,
                FOREIGN KEY (numero_installation) REFERENCES installation(numero)
                )
            """)

            cursor.execute("""CREATE TABLE IF NOT EXISTS activite(
                id INTEGER PRIMARY KEY,
                numero_activites INTEGER,
                numero_equipements INTEGER,
                desc_act TEXT,
                nom TEXT,
                FOREIGN KEY (numero_equipements) REFERENCES equipements(numero_equipements)
                )
            """)

            conn.commit()
            printerr('table "adresse" successfully created')
            printerr('table "installation" successfully created')
            printerr('table "equipement" successfully created')
            printerr('table "activite" successfully created')
            printerr('database successfully created')
        except Exception as e:
            printerr(type(e))
            printerr('exception ocurred while creating database')
            printerr("-------------------------")
            printerr(e)
            conn.rollback()
        finally:
            conn.close()






def clear_db():
    '''
    Purge entièrement la base de données
    '''

    if os.path.exists(DB_FULLPATH):
        try:
            printerr('starting database emptying')
            conn = sqlite3.connect(DB_FULLPATH)
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
            printerr('database emptied successfully')
        except Exception as e:
            conn.rollback()
            printerr(type(e))
            printerr('exception occurred while emptying database')
            printerr('==============')
            printerr(e)
        finally:
            conn.close()
