import json

data = [];

i = 0;

with open('data.json') as f:
	for line in f:

		j_content = json.loads(line)

		if j_content['type'] == 'business':

			if 'Bars' in j_content['categories']:

				print(j_content)