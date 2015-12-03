import json

data = [];

i = 0;

lat_long_rate = open('latlongrate.txt', 'w');

with open('data.json') as f:
	for line in f:

		j_content = json.loads(line)

		if j_content['type'] == 'business':

			lat_long_rate.write(str(j_content['latitude'])+ ' ' +str(j_content['longitude']) + ' ' +str(j_content['stars']) + '\n')

lat_long_rate.close()


