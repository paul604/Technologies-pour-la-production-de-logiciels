from ....database.dao.dao.dao_equipement import *
from ....database.dao.dao.dao_activite import a_get_nums
from ...lib.bottle import route, request
from ...lib.utils import *



# -------------------------------------------------------- équipements
@route('/data/equipements')
def e_route():
	'''
	Liste les équipements où l'on peut pratiquer l'activité dont le nom exact (`request.query.activite`) est passé en GET
	'''	
	if request.query.activite != '':
		equipements = set()
		for num in a_get_nums(request.query.activite): # ce set de `numero_equipements` contient les ID des équipements à renvoyer
			equipements = equipements | e_get_object_by_id(str(num[0])) # ajout des éléments du set de retour dans notre set de résultat ("|"" c'est l'union des deux ensembles)
		return set_of_objects2json(equipements)

	'''
	Récupère tous les équipements ou un équipement en particulier si l'id est spécifié
	'''
	return set_of_objects2json(e_get_object_by_id(request.query.id or -1))
