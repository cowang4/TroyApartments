
from craigslist import CraigslistHousing
import dist
from csv import *

cl = CraigslistHousing(site='albany', category='apa',
                         filters={'max_price': 2000, 'min_price': 500})

results = cl.get_results(sort_by='newest', geotagged=True) # limit=100
#for result in results:
#    print result

troy_results = []
for result in results:
    if (result['name'] is not None and 'troy' in result['name'].lower()) or (result['where'] is not None and 'troy' in result['where'].lower()):
        troy_results.append(result)

RPI_coords = (42.729376, -73.677912)
for result in troy_results:
    if result['geotag'] is not None:
        print result
        print result['geotag']
        distance = dist.points2distance(result['geotag'], RPI_coords)
        result['dist'] = distance
        print distance

with open('apartments.csv', 'w') as csvfile:
    fieldnames = ['name', 'has_image', 'url', 'has_map', 'price', 'geotag', 'where', 'id', 'datetime', 'dist']
    writer = DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in troy_results:
        writer.writerow(result)
