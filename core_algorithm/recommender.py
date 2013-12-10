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


def recommend(class_id, latitude, longitude, num = 3):
	module_dir = os.path.dirname(__file__)  # get current directory
	# file_path = os.path.join(module_dir, 'baz.txt')
	data = read_data(os.path.join(module_dir,'classifiedParks.json'))

	# logging.error(len(data))
	parks = data[class_id][str(class_id)]
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

def calDistanceN(la1, lo1, p):
	MAX_DIST = 99999
	R = 6371
	# print p['latitude']
	if p['latitude'] != "":
		la2 = float(p['coords']['lat'])
		lo2 = float(p['coords']['lon'])
		dLat = rad(la1 - la2)
		dLong = rad(lo1 - lo2)
		a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(rad(la1)) * math.cos(rad(la2)) * math.sin(dLong/2) * math.sin(dLong/2)
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
		d = R * c
		return d
	else:
		return MAX_DIST

def recommendN(class_id, latitude, longitude):
	# skiing
    class1 = [2,5,7,11,15,21,23,50,57]
    # hunting, general tour
    class2 = [3,8,20,24,36,38,41,44,54,10,17,48,30,32,27]
    # caneoing, kayalaying
    class3 = [6,18,19,26,29,39,45,46,51,52, 56]
    # biking
    class4 = [16,28,31,33,37,42,43,49,53,50,10]
    # horse riding
    class5 = [0,1,4,9,12,13,22,25,55,34,35,40]
    classes = []
    classes.append(class1)
    classes.append(class2)
    classes.append(class3)
    classes.append(class4)
    classes.append(class5)

    module_dir = os.path.dirname(__file__)  # get current directory
	# file_path = os.path.join(module_dir, 'baz.txt')
	Ndata = read_data(os.path.join(module_dir,'NparkDetails.json'))
	Nparks = [Ndata[i] for i in classes[int(class_id)]]
	distances = [calDistanceN(latitude, longitude, p ) for p in Nparks]
	idx = distances.index(min(distances))
	return Nparks[idx]



if __name__ == "__main__":
	res = recommend(2, 38.65, 43.1141667)
	print res
	



