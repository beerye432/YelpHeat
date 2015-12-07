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

			if 'Restaurants' in j_content['categories'] or 'Food' in j_content['categories'] or 'Bars' in j_content['categories']:
				rating = float(j_content['stars'])

				name = str(j_content['schools'])
				
				numRate = int(j_content['review_count']

				reviews = int(j_content['review_count'])

				if name in schools:
					total_rate = schools[name][0]
					total_num = schools[name][1]
					total_rev = schools[name][2]
					schools[name] = (total_rate + rating, total_num + 1, total_rev + reviews)
				else:
					schools[name] = (rating, 1, reviews)

				lat_long_rate.write(str(j_content['latitude'])+ ' ' +str(j_content['longitude']) + ' ' + str(j_content['stars']/5) + '\n')


for school in schools:
	school_average.write(str(school) + ' Average: ' + str("{0:.3f}".format(schools[school][0]/schools[school][1])) + ' Total Reviews: ' + str(schools[school][2]) + '\n')

school_average.close()

lat_long_rate.close()
