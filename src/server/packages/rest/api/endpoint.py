'''
Met à disposition un service web de récupération de de données en JSON à l'aide de la librairie bottle.
http://bottlepy.org/docs/dev/tutorial.html




i_XX   relatif à une installation
e_XX   relatif à un équipement
a_XX   relatif à une activité





Exemple de la forme du JSON final (node data)

{
	"data":[
		{"id":"id1","nom":"nom1","adresse":"adresse1","code_postal":"code_postal1","ville":"ville1"},
		{"id":"id2","nom":"nom2","adresse":"adresse2","code_postal":"code_postal2","ville":"ville2"},
		{"id":"id3","nom":"nom3","adresse":"adresse3","code_postal":"code_postal3","ville":"ville3"}
	]
}
'''



from ..lib.bottle import route, run, request
from ..lib.utils import *
from ...database.dao.dao.dao_installation import *
from ...database.dao.dao.dao_equipement import *
from ...database.dao.dao.dao_activite import *
from ...database.dao.dao.dao_ville import *



def launch_rest_api_service(host='localhost', port=1234, debug=False):
	'''
	Permet le lancement du serveur bottle
	'''
	run(host=host, port=port, debug=debug)



# ||||||||||||||||||||||||||||||||||||||||||||||||| Définition de routes dynamiques : accès aux données en fonction de la structure de l'URL + paramètres GET
# =========================================== villes



@route('/data/villes')
def get_villes():

	'''
	Récupère les villes matchant la recherche
	'''
	if request.query.ville != '':

		results = []
		ville_simplified_input = simplify(request.query.ville)
		ville_db_name = ''
		
		for v in v_getall():
			vstring = str(v[0])
			if ville_simplified_input in simplify(vstring):
				ville_db_name = vstring
				results.append(ville_db_name)

		return list2json(results)

	'''
	Récupère la liste des villes
	'''
	return list_of_tuples2json(v_getall())



@route('/data/codes_postaux')
def get_codes_postaux():

	'''
	Récupère les codes postaux matchant la recherche
	'''
	# if request.query.cp != '':

	# 	results = []		
	# 	for v in v_getall():
	# 		vstring = str(v[0])
	# 		if ville_simplified_input in simplify(vstring):
	# 			ville_db_name = vstring
	# 			results.append(ville_db_name)

		# return list2json(results)

	'''
	Récupère la liste des codes postaux
	'''
	return list_of_tuples2json(cp_getall())



@route('/data/cp_et_v')
def get_cp_and_v():
	'''
	Récupère la liste des villes et leurs codes postaux associés
	'''
	return list_of_tuples2json(cp_and_v_getall())



# =========================================== installations



@route('/data/installations')
def get_i(i_id = -1):


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
	Récupère toutes les installations ou une installation en particulier si l'i_id est spécifié
	'''
	return set_of_objects2json(i_get_object_by_id(request.query.id or i_id))



#  ================================================ autres



@route('/data/equipements')
def get_e(e_id = -1):
	'''
	Récupère tous les équipements ou un équipement en particulier si l'e_id est spécifié
	'''
	return set_of_objects2json(e_get_object_by_id(request.query.id or e_id))



@route('/data/activites')
def get_a(a_id = -1):
	'''
	Récupère toutes les activitées ou une activité en particulier si l'a_id est spécifié
	'''
	return set_of_objects2json(a_get_object_by_id(request.query.id or a_id))









