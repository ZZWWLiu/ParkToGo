# core algorithm
# content-based recommender
# recommend parks to customer C that are similar to parks that rate highly by C.

# give customer five parks to rate: YellowStone, Yosemite, Grand Caneo, gongmen, Alaska
import urllib2
from xml.dom import minidom
import time
import json
import os

# query = 'pstate='+states[0]
# camp_search = 'http://api.amp.active.com/camping/campgrounds?'+query+'&api_key='+key

def read_data(filename):
    """
    purpose: read from the json file.
    parameter: 
        filename - the path of json file in your local computer 
    return: a dictionary
    """
    data = {}
    try:
        with open(filename) as f:
        	for line in f:
	        	data = json.loads(line.strip())
    except:
        print "Failed to read data!"
        return {}
    print "The json file has been successfully read!"
    return data

def collectParkInfo(states, filename = 'parkIDs.json'):
	f = open(filename, "w")
	key = 'd2rttztqpfhbqjz42buq6duc'
	ParkIDs = {}
	for state in states:
		query = 'pstate='+state
		camp_search = 'http://api.amp.active.com/camping/campgrounds?'+query+'&api_key='+key
		urlfile = urllib2.urlopen(camp_search)
		data = urlfile.read()
		urlfile.close()
		# parse the xml
		dom = minidom.parseString(data)
		resultlist = dom.getElementsByTagName('result')
		facilityIDlist = []
		contractTypelist = []
		# facilityNamelist = []
		# we only cares about the state parks (others do not have a detail info)
		for s in resultlist:
			if s.attributes['contractType'].value == 'STATE':
				facilityIDlist.append(s.attributes['facilityID'].value)
				# facilityNamelist.append(s.attributes['facilityName'].value)
		if len(facilityIDlist) > 0:
			ParkIDs[state] = facilityIDlist
		time.sleep(1)
	f.write(json.dumps(ParkIDs))
	f.close()
	return ParkIDs

def collectParkDetail(parkIds, filename = 'parkDetails.json'):
	f = open(filename, "w")
	key = 'd2rttztqpfhbqjz42buq6duc'
	for state in parkIds:
		for parkid in parkIds[state]:
			parkDetails = {'facilityID':parkid,'state': state}  # {parkid: {'state': 'CA', 'amenity': ['xx', 'xxx']}}
			query = 'contractCode='+state+'&parkId='+parkid
			camp_detail = 'http://api.amp.active.com/camping/campground/details?'+query+'&api_key='+key
			urlfile = urllib2.urlopen(camp_detail)
			data = urlfile.read()
			urlfile.close()
			dom = minidom.parseString(data)
			amenities = dom.getElementsByTagName('amenity')
			amenityList = []
			for a in amenities:
				amenityList.append(a.attributes['name'].value)
			parkDetails['amenity'] = amenityList
			f.write(json.dumps(parkDetails) + '\n')
			time.sleep(0.5)
	f.close()

if __name__ == "__main__":
# 	states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL",
# "GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS",
# "MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI",
# "SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
	# print 'ready to collect park IDs..'
	# parkIDs = collectParkInfo(states)
	# print 'collect IDs done!'
    parkIDs = read_data(os.path.join(os.getcwd(),'parkIDs.json'))
    collectParkDetail(parkIDs)
    # small_sample = {'DE': parkIDs['DE']}
    # print 'ready to collect park details'
    # collectParkDetail(small_sample)
    # num = 0
    # for state in parkIDs:
    # 	num += len(parkIDs[state])
    # print num



