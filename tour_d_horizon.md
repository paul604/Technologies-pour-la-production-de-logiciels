### Petit mémo-guide pour présentation orale informelle
## Structure du projet

* `tree -d` découpage systématique en dossiers -> rendre le projet facilement scalable
* `src/server` --- séparé de --- `src/client`
* découpage certes fin mais explicite, naviguer dans l'arborescence est similaire à une recherche du plus général au plus spécifique

## Mécanismes d'`import`

* [(re)lectures attentives de la PEP 328](https://www.python.org/dev/peps/pep-0328/)
* utilisation d'un fichier `config.py` (fait également office de fichier `utils.py`), placé dans le package de plus haut niveau (=="top-level-package") pour diffuser des variables ou fonctions nécessitant un accès dans l'ensemble du projet
* utilisation des imports relatifs pour les besoins habituels `from .my_package.my_module_py_file import my_method`

## Choix effectués

* "au plyus simple" entre pragmatique et factorisé -> `config.py` mais 3 `csv2db_xxx.py`
* parti pris de gérer les matchs suggestions/recherches en python et non en couche base de données pour avoir une souplesse de traitement
* sqlite3 pour la facilité de déploiement (y'en a pas !) plutôt que MySQL

## Limites

* volume des données : traitements pythons plus riches et lents qu'en BDD, mais avant que la lenteur soit un problème, sqlite3 aura aussi atteint ses limites
* si augmentation plus avant du projet, des méthodes wrappers seront nécessaires dans les routes : diviser pour régner. plus la taille augmente, plus il est nécessire de factoriser (classe CSVMGR relative à toutes les gestions CSV, par exemple)

## Conclusion

Projet relativement propre/structuré/modulable pour sa taille, mais changements nécessaires si désir de l'étendre, ou, à l'inverse, de le tourner en "projet POC" auxquel cas il faudrait "dépaqueter" le code.
