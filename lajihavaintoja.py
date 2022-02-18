import requests
from requests.structures import CaseInsensitiveDict
import json
import re
import random
import config

def start():

	listattu = []

	page = random.randint(1, 4280)
	print(page)
	url = f"https://api.laji.fi/v0/warehouse/query/unit/list?pageSize=1000&page={page}&cache=false&useIdentificationAnnotations=true&includeSubTaxa=true&includeNonValidTaxa=true&individualCountMin=1&qualityIssues=NO_ISSUES&access_token={config.access_token}"

	headers = CaseInsensitiveDict()
	headers["Accept"] = "application/json"

	resp = requests.get(url, headers=headers)
	data = json.loads(resp.content.decode('utf-8'))
	results = data['results']

	for i in results:
		if 'linkings' in i['unit'].keys() and 'taxon' in i['unit']['linkings'].keys() and 'vernacularName' in i['unit']['linkings']['taxon'].keys() and 'notes' in i['unit'].keys() and len(i['unit']['notes']) > 15 and len(i['unit']['notes']) < 170:
			try:
				nimi = i['unit']['linkings']['taxon']['vernacularName']['fi']
				notes = i['unit']['notes']
				aika = i['gathering']['displayDateTime']
				parsedAika = re.split('[-| ]',aika)
				paikka = i['gathering']['interpretations']['municipalityDisplayname']
				listaa = (f'#{nimi.capitalize()}\n"{notes.capitalize()}"\n#{paikka} {parsedAika[2]}.{parsedAika[1]}.{parsedAika[0]}')
				listattu.append(listaa)

			except (KeyError, IndexError):
				start()

	print(random.choice(listattu))

start()
