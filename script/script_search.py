import os, json, sys

file_corpus_majinbook = 'corpus/majinbook_fra.jsonl'

def normalize_data(data):
	results = []

	#Transforme les différents formats en str
	if isinstance(data, str):
		results.append(data)

	# ou int
	elif isinstance(data, (int, float)):
		results.append(str(data))
		
	elif isinstance(data, list):
		for item in data:
			# si forme json est double liste [[id, "Nom"]]
			if isinstance(item, list) and len(item) > 1:
				# choix item 1 (nom auteur par ex)
				if isinstance(item[1], str):
					results.append(item[1])
				elif isinstance(item, str):
					results.append(item)
			else:
				results.append(str(item))

	return results


def search_JSON(key, query):
	matches = []
	num = 1

	#Fonction de recherche
	with open(file_corpus_majinbook, 'r', encoding='utf-8') as f:
		for line in f:
			# read JSON line and convert it into Py object
			item = json.loads(line)

			# get key value 
			value = item.get(key)

			if value is None:
				continue

			# Applique fonction normalisation
			normalized = normalize_data(value)

			for text in normalized:
				if query.lower() in text.lower():
					matches.append(item)
					break

	if not matches:
		print("No match found")
	else:
		for num, x in enumerate(matches, start=1):
			print(f"- Result {num} : {x}\n")

	

search_JSON("authors", "Michon")
