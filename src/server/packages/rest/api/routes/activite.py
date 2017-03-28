from ....database.dao.dao.dao_equipement import *
from ...lib.bottle import route, request
from ...lib.utils import *



# -------------------------------------------------------- activitées
@route('/data/activites')
def a_route():
	'''
	Récupère toutes les activitées ou une activité en particulier si l'id est spécifié
	'''
	return set_of_objects2json(a_get_object_by_id(request.query.id or -1))
