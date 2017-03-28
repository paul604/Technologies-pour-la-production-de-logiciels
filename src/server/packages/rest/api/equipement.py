from ...database.dao.dao.dao_equipement import *
from ..lib.bottle import route, request
from ..lib.utils import *



# -------------------------------------------------------- équipements
@route('/data/equipements')
def e_route():
	'''
	Récupère tous les équipements ou un équipement en particulier si l'id est spécifié
	'''
	return set_of_objects2json(e_get_object_by_id(request.query.id or -1))
