# recommend 3 parks to user
import json
import os
import math
import logging


def read_data(filename):
    """
    Used to read all tweets from the json file.
    """
    data = []
    try:
        with open(filename) as f:
            for line in f:
                data.append(json.loads(line.strip()))
    except:
        print "Failed to read data!"
        return []
    # print "The json file has been successfully read!"
    return data


def rad(x):
	return x*3.14156/180

def calDistance(la1, lo1, p):
	MAX_DIST = 99999
	R = 6371
	# print p['latitude']
	if p['latitude'] != "":
		la2 = float(p['latitude'])
		lo2 = float(p['longitude'])
		dLat = rad(la1 - la2)
		dLong = rad(lo1 - lo2)
		a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(rad(la1)) * math.cos(rad(la2)) * math.sin(dLong/2) * math.sin(dLong/2)
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
		d = R * c
		return d
	else:
		return MAX_DIST


def recommend(cluster_id, latitude, longitude, num = 3):
	module_dir = os.path.dirname(__file__)  # get current directory
	# file_path = os.path.join(module_dir, 'baz.txt')
	data = read_data(os.path.join(module_dir,'parkclusters.json'))
	logging.error(len(data))
	parks = data[cluster_id][str(cluster_id)]
	# print parks
	distances = [calDistance(latitude, longitude, p ) for p in parks]
	# distances = [calDistance(latitude, longitude, float(p['latitude']), float(p['longitude']) for p in parks]
	ordered_dis = sorted(distances)
	res = []
	for i in xrange(num):
		# print ordered_dis[i]
		idx = distances.index(ordered_dis[i])
		res.append(parks[idx])
	return res


if __name__ == "__main__":
# 	introduction = 'Arches National Park\n\
# This site features more than 2,000 natural sandstone arches, including the Delicate Arch. In a desert climate millions of years of erosion have led to these structures, and the arid ground has life-sustaining soil crust and potholes, natural water-collecting basins. Other geologic formations are stone columns, spires, fins, and towers.\
# \n \
# Glacier National Park\n\
# Part of Waterton Glacier International Peace Park, this park has 26 remaining glaciers and 130 named lakes under the tall Rocky Mountain peaks. There are historic hotels and a landmark road in this region of rapidly receding glaciers. These mountains, formed by anoverthrust, have the world\'s best sedimentary fossils from the Proterozoic era.\n \
# Hawaii Volcanoes National Park\n\
# This park on the Big Island protects the Kilauea and Mauna Loa volcanoes, two of the world\'s most active. Diverse ecosystems of the park range from those at sea level to 13,000 feet (4,000 m).\
# \n\
# Great Smoky Mountains National Park\n\
# The Great Smoky Mountains, part of the Appalachian Mountains, have a wide range of elevations, making them home to over 400 vertebrate species, 100 tree species, and 5000 plant species. Hiking is the park\'s main attraction, with over 800 miles (1,300 km) of trails, including 70 miles (110 km) of the Appalachian Trail. Other activities are fishing, horseback riding, and visiting some of nearly 80 historic structures.\
# \n\
# Yellowstone National Park\n\
# Situated on the Yellowstone Caldera, the first national park in the world has vast geothermal areas such as hot springs and geysers, the best-known being Old Faithful and Grand Prismatic Spring. The yellow-hued Grand Canyon of the Yellowstone River has numerouswaterfalls, and four mountain ranges run through the park. There are almost 60 mammal species, including the gray wolf, grizzly bear,lynx, bison, and elk.'
# 	print introduction
# 	print 'please rate those five Parks : (enter 1~5)'
	# rate1 = raw_input('Arches National Park : ')
	# rate2 = raw_input('Glacier National Park : ')
	# rate3 = raw_input('Hawaii Volcanoes National Park : ')
	# rate4 = raw_input('Great Smoky Mountains National Park : ')
	# rate5 = raw_input('Yellowstone National Park : ')
	# rateList = [rate1, rate2, rate3, rate4, rate5]
	# num = rateList.index(max(rateList))
# print num
	# data = read_data(os.path.join(os.getcwd(),'parkclusters.json'))
	# parks = data[num][str(num)]
	# print 'recommended parks:'
	# for i in xrange(3):
	# 	print parks[i]
	res = recommend(2, 38.65, 43.1141667)
	print res
	



