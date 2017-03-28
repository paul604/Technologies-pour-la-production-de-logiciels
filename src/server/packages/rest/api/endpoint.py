from ..lib.bottle import run




# /!\ ne pas retirer /!\
# imports servant à charger les routes
from .routes.installation import i_route
from .routes.equipement import e_route
from .routes.activite import a_route
from .routes.ville import *



'''
Met à disposition un service web de récupération de de données en JSON à l'aide de la librairie bottle
http://bottlepy.org/docs/dev/tutorial.html

i_XX   relatif à une installation
e_XX   relatif à un équipement
a_XX   relatif à une activité
'''



def launch_rest_api_service(host='localhost', port=1234, debug=False):
	'''
	Permet le lancement du serveur bottle
	'''
	run(host=host, port=port, debug=debug)
