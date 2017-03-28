from ....database.dao.dao.dao_equipement import *
from ...lib.bottle import route, request
from ...lib.utils import *



# -------------------------------------------------------- équipements
@route('/data/equipements')
def e_route():
	'''
	Récupère les équipements où l'on peut pratiquer l'activité dont le nom exact est passé en GET


	########### Lister les installations (ou les équipements) où l'on peut pratiquer une activité donnée.
	##### Premier jet de pseudo-pseudo-grossier-code, mais l'idée de base est là
	aaa = list(activités).contains(nom)
	bbb = list(numero_activites) // obtenue via aaa requery sur la table `activites` via fonction en @private
	ccc = set()
	list(équipements).filter(foreach(b in bbb){select where numero_equipements=b; on l'add à ccc})
	return ccc;


	'''
	if request.query.nom != '':
		return set_of_objects2json(e_get_object_by_num_equip(a_get_num_from_nom(request.query.nom)))

	'''
	Récupère tous les équipements ou un équipement en particulier si l'id est spécifié
	'''
	return set_of_objects2json(e_get_object_by_id(request.query.id or -1))
