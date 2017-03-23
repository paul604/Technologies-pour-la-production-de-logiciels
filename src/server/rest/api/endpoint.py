
'''
Met à disposition un service web de récupération de de données en JSON à l'aide de la librairie bottle.
'''


from rest.lib.bottle import route, run


def launch_rest_api_service():
	run(host='localhost', port=1234, debug=True) # ne pas utiliser 80 ou 8080 (déjà utilisés)


# méthode de test
@route('/')
def hello():
    return "Hello World!"

