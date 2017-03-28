from ....database.dao.dao.dao_activite import *
from ...lib.bottle import route, request
from ...lib.utils import *



# -------------------------------------------------------- activités
@route('/data/activites')
def a_route():
	'''
	Récupère les activités matchant la recherche
	'''
	if request.query.suggestions != '':

		results = set()
		activite_simplified_input = simplify(request.query.suggestions)
		
		for a in a_get_object_by_id():
			if activite_simplified_input in simplify(a.nom):
				results.add(a.nom) # results étant un set, les doublons s'éliminent d'eux-mêmes

		return list2json(list(results))


	'''
	Récupère les activités d'un numéro `numero` donné en GET
	'''
	if request.query.numero != '':
		return set_of_objects2json(a_get_object_by_num_act(request.query.numero))


	'''
	Récupère toutes les activités ou une activité en particulier si l'id est spécifié
	'''
	return set_of_objects2json(a_get_object_by_id(request.query.id or -1))
