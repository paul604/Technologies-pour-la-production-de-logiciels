from ...database.dao.dao.dao_installation import *
from ..lib.bottle import route, request
from ..lib.utils import *



'''
Exemple de la forme du JSON final (node data)

{
	"data":[
		{"id":"id1","nom":"nom1","adresse":"adresse1","code_postal":"code_postal1","ville":"ville1"},
		{"id":"id2","nom":"nom2","adresse":"adresse2","code_postal":"code_postal2","ville":"ville2"},
		{"id":"id3","nom":"nom3","adresse":"adresse3","code_postal":"code_postal3","ville":"ville3"}
	]
}
'''




# -------------------------------------------------------- installations
@route('/data/installations')
def i_route():
	'''
	Récupère toutes les installations des villes matchant la recherche
	'''
	if request.query.ville != '':

		results = set()
		ville_simplified_input = simplify(request.query.ville)
		ville_db_name = ''
		
		for v in v_getall():
			vstring = str(v[0])
			if ville_simplified_input in simplify(vstring):
				ville_db_name = vstring
				results.add(set_of_objects2json(i_get_object_by_ville(ville_db_name)))

		return results


	'''
	Récupère toutes les installations aux codes postaux correspondants
	'''
	if request.query.cp != '':
		results = set()
		
		for cp in cp_getall():
			cpstring = str(cp[0])
			if request.query.cp in cpstring:
				results.add(set_of_objects2json(i_get_object_by_cp(cpstring)))

		return results
	

	'''
	Récupère toutes les installations ou une installation en particulier si l'id est spécifié
	'''
	return set_of_objects2json(i_get_object_by_id(request.query.id or -1))
