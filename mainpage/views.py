# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from mainpage.models import UserParkForm, LocationForm
import urllib2
from xml.dom import minidom
import logging
import time
import json
from core_algorithm import recommender, pyipinfodb
from google.appengine.api import memcache
from google.appengine.api import urlfetch

# import re
# import hashlib
# photo url = http://www.reserveamerica.com/webphotos/CO/pid50032/5/180x120.jpg
# src = http://www.reserveamerica.com + webphoto

# it's better to store all the parks info in database
def getResDetail(res):
	key = 'd2rttztqpfhbqjz42buq6duc'
	baseUrl = 'http://www.reserveamerica.com'
	resDetail = []
	for r in res:
		detail = {}
		query = 'contractCode='+r['state']+'&parkId='+r['facilityID']
		camp_detail = 'http://api.amp.active.com/camping/campground/details?'+query+'&api_key='+key
		urlfile = urllib2.urlopen(camp_detail)
		data = urlfile.read()
		urlfile.close()
		dom = minidom.parseString(data)
		detailDescription = dom.getElementsByTagName('detailDescription')
		detail['description'] = detailDescription[0].attributes['description'].value
		detail['facility'] = detailDescription[0].attributes['facility'].value
		detail['importantInformation'] = detailDescription[0].attributes['importantInformation'].value
		photoUrls = []
		photos = dom.getElementsByTagName('photo')
		for p in photos:
			realUrl = p.attributes['realUrl'].value
			# logging.error(realUrl)
			if realUrl != '':
				photoUrls.append(baseUrl+realUrl)
		detail['imgs'] = photoUrls
		detail['state'] = r['state']
		resDetail.append(detail)
		time.sleep(0.6)
	return resDetail

def weatherForcast(lat, lon):
	"""OpenWeatherMap API
	   Input: lat and lon String
	   Output: dict of weather info
	"""
	api_key = '9f282f36bbd552d28d07769dcb3e7019'
	query = '&lat='+lat+'&lon='+lon+'&APPID='+api_key
	Url = 'http://api.openweathermap.org/data/2.5/forecast/daily?cnt=10&mode=json'+query
	urlfile = urllib2.urlopen(Url)
	data = urlfile.read()
	urlfile.close()
	# parse the json
	datadict = json.loads(data)
	return datadict


def homepage(request):
	if request.method == 'GET':
		urlfetch.set_default_fetch_deadline(45)
		ip_api_key = '97f4d203b989b3fe87045b255e7a29d42f403cafc8726c45172079dbaa60fbfe'
		ipinfo = pyipinfodb.IPInfo(ip_api_key)
		# ip = ipinfo.GetPublicIp()
		ip = '165.91.11.22'
		memcache.set('ip', ip)
		# logging.error(ip)
		# use clients' public ip address to find their locations
		dataDict = memcache.get(ip)
		if dataDict is None:
			dataDict = ipinfo.GetCity(ip = ip)
			memcache.set(ip, dataDict)
		lat = dataDict["latitude"]
		lon = dataDict["longitude"]
		logging.error(dataDict)
		API_KEY = 'AIzaSyAnEt9j1iiUDG6X2cRxQ2GUfotwoe4vCCY'
		google_maps = "https://maps.googleapis.com/maps/api/js?key="+API_KEY+"&sensor=false"
		content = {'google_maps_src': google_maps ,
		           'latitude' : float(lat),
		           'longitude' : float(lon)
		           }
		return render(request, 'mainpage/userform.html', content)

def submit(request):
	if request.method == 'POST':
		urlfetch.set_default_fetch_deadline(45)
		form = LocationForm(request.POST)
		if form.is_valid():
			user_need = form.cleaned_data
			ip = memcache.get('ip')
			# logging.error(ip)
			if user_need['coordinates'] is None:
				dataDict = memcache.get(ip)
				lat = float(dataDict["latitude"])
				lon = float(dataDict["longitude"])
			else:
				coord = user_need['coordinates'].split(',')
				lat = float(coord[0])
				lon = float(coord[1])
			res = recommender.recommend(0, lat, lon)
			resDetail = getResDetail(res)
			API_KEY = 'AIzaSyAnEt9j1iiUDG6X2cRxQ2GUfotwoe4vCCY'
			google_maps = "https://maps.googleapis.com/maps/api/js?key="+API_KEY+"&sensor=false"
			content = {'results': resDetail,
					   'google_maps_src': google_maps ,
		               'latitude' : lat,
		               'longitude' : lon,
		               'lat1': float(res[0]['latitude']),
		               'lon1': float(res[0]['longitude']),
		               'lat2': float(res[1]['latitude']),
		               'lon2': float(res[1]['longitude']),
		               'lat3': float(res[2]['latitude']),
		               'lon3': float(res[2]['longitude'])}
			return render(request, 'mainpage/recommend.html', content)













