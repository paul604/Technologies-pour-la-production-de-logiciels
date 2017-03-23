class Equipement:
    '''
    Classe représentant un équipement.
    '''

    def __init__(self, id, nom, numero_installation, latitude, longitude):
        self.id = id
        self.nom = nom
        self.numero_installation = numero_installation
        self.latitude = latitude
        self.longitude = longitude
