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
	res = recommend(2, 38.65, 43.1141667)
	print res
	



