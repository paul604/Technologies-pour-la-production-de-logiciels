'''
Fournit un ensemble de méthodes utilitaires relatives à l'export en JSON
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
	return to_json('['+','.join(l)+']')



def list_of_tuples2json(l):
	'''
	Construit une string JSON à partir d'une liste de tuples
	'''
	return to_json('['+','.join(['"'+' '.join([str(_) for _ in v])+'"' for v in l])+']')



def list2json(l):
	'''
	Construit une string JSON à partir d'une liste d'éléments
	'''
	return to_json('['+','.join(['"'+''.join([str(_) for _ in v])+'"' for v in l])+']')



def to_json(s):
	'''
	Termine la construction JSON (englobement sous une node data que l'on crée ici)
	'''
	return '{"data":' + s + '}'



def simplify(string):
	'''
	Enlève les caractères utf8 ainsi que les accents et les remplace par leurs équivalents ascii
	'''
	return ''.join((c for c in unicodedata.normalize('NFD', string.lower()) if unicodedata.category(c) != 'Mn'))