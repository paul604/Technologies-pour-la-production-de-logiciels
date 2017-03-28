'''
Fournit un ensemble de méthodes utilitaires
'''



import json, unicodedata



def set_of_objects2json(s):
	'''
	Construit une string JSON représentative à partir d'un set d'objets
	'''
	return list_of_objects2json([json.dumps(o.__dict__, ensure_ascii=False) for o in s])



def list_of_objects2json(l):
	'''
	Construit une string JSON à partir d'une liste d'objets sérialisables
	'''
	return '{"data":['+','.join(l)+']}'



def list_of_tuples2json(l):
	'''
	Construit une string JSON à partir d'une liste de tuples
	'''
	return '{"data":['+','.join(['"'+' '.join([str(_) for _ in v])+'"' for v in l])+']}'



def list2json(l):
	'''
	Construit une string JSON à partir d'une liste d'éléments
	'''
	return '{"data":['+','.join(['"'+''.join([str(_) for _ in v])+'"' for v in l])+']}'



def simplify(string):
	'''
	Enlève les caractères utf8 ainsi que les accents et les remplace par leurs équivalents ascii
	'''
	return ''.join((c for c in unicodedata.normalize('NFD', string.lower()) if unicodedata.category(c) != 'Mn'))