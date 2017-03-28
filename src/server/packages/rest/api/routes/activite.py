from ....database.dao.dao.dao_activite import *
from ...lib.bottle import route, request
from ...lib.utils import *



# -------------------------------------------------------- activitées
@route('/data/activites')
def a_route():
	'''
	Récupère les activitées matchant la recherche
	'''
	if request.query.activite != '':

		results = set()
		activite_simplified_input = simplify(request.query.activite)
		
		for a in a_get_object_by_id():
			if activite_simplified_input in simplify(a.nom):
				results.add(a)

		return set_of_objects2json(results)


	'''
	Récupère les activitées d'un numéro `numero` donné en GET
	'''
	if request.query.numero != '':
		return set_of_objects2json(a_get_object_by_num_act(request.query.numero))




	'''
	Récupère toutes les activitées ou une activité en particulier si l'id est spécifié
	'''
	return set_of_objects2json(a_get_object_by_id(request.query.id or -1))
