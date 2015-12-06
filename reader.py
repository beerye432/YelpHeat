import json

data = [];

i = 0;

school_average = open('school_average.txt', 'w')

lat_long_rate = open('latlongrate.txt', 'w')

schools = dict()

with open('data.json') as f:
	for line in f:

		j_content = json.loads(line)

		if j_content['type'] == 'business':

			if 'Restaurants' in j_content['categories']:
				rating = float(j_content['stars'])

				name = str(j_content['schools'])

				if name in schools:
					total_rate = schools[name][0]
					total_num = schools[name][1]
					schools[name] = (total_rate + rating, total_num + 1)
				else:
					schools[name] = (rating, 1)

				lat_long_rate.write(str(j_content['latitude'])+ ' ' +str(j_content['longitude']) + '\n')

				i = i + 1;

for school in schools:
	print(schools[school][1])
	school_average.write(str(school) + ' ' + "{0:.3f}".format(schools[school][0]/schools[school][1]) + '\n')


print(i)


school_average.close()


