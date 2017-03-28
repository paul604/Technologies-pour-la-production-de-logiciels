from ....database.dao.dao.dao_ville import *
from ...lib.bottle import route, request
from ...lib.utils import *





# -------------------------------------------------------- villes
@route('/data/villes')
def v_route():
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





# -------------------------------------------------------- codes postaux
@route('/data/codes_postaux')
def cp_route():
	'''
	Récupère les codes postaux matchant la recherche
	'''
	#TODO
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





# -------------------------------------------------------- codes postaux + villes
@route('/data/cp_et_v')
def cp_et_v_route():
	'''
	Récupère la liste des villes et leurs codes postaux associés
	'''
	return list_of_tuples2json(cp_and_v_getall())
