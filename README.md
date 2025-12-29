# A search engine for MajinBook
A search engine dedicated to json files, and MajinBook corpus

# Note :

Premier jet du script. Pour l'instant le code n'est pas très robuste.
- Le filtrage est fermé : possibilité de chercher uniquement une paire clef, item.
- >> ajouter un couplage des arguments de filtrage, par exemple `genre` + `title` + `1870`.

## Utilisation :

Utiliser la fonction `search_JSON()` afin de rechercher des tokens dans le JSON.
- La fonction attend deux arguments : `search_JSON(key, query)`

### Liste `key`:
- first_pub_year
- authors
- genres
- n_reviews
- n_ratings
- rating
- title
- work_id
- zlibrary_ids
- libgen_ids

### Arguments `query` :
- Attend un filtrage précis, par exemple un nom d'auteur, un genre, une note.

### Recherche possible :
```
search_JSON("authors", "Michon")

>>> - Result 1 : {'first_pub_year': 2002, 'authors': [[144614, 'Pierre Michon']], 'genres': ['Nonfiction', 'France'], 'n_reviews': 13, 'n_ratings': 96, 'rating': 3.62, 'title': 'Corps du roi', 'work_id': 712335, 'zlibrary_ids': [12112944, 21821990, 24020675, 12112948, 18714090, 13303251], 'libgen_ids': ['f07b6f752545092eefccaa095e82f631']}
```
