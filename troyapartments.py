
from craigslist import CraigslistHousing
import dist

cl = CraigslistHousing(site='albany', category='apa',
                         filters={'max_price': 2000, 'min_price': 500})

results = cl.get_results(sort_by='newest', geotagged=True, limit=100)
#for result in results:
#    print result

troy_results = []
for result in results:
    if (result['name'] is not None and 'Troy' in result['name']) or (result['where'] is not None and 'Troy' in result['where']):
        troy_results.append(result)

RPI_coords = (42.729376, -73.677912)
for result in troy_results:
    if result['geotag'] is not None:
        print result
        print result['geotag']
        print dist.points2distance(result['geotag'], RPI_coords)
