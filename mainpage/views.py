# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from mainpage.models import UserParkForm
import urllib2
from xml.dom import minidom
# from django.core.cache import cache
import logging
import pyipinfodb
from core_algorithm import recommender
from google.appengine.api import memcache
# import re
# import hashlib
# photo url = http://www.reserveamerica.com/webphotos/CO/pid50032/5/180x120.jpg
# src = http://www.reserveamerica.com + webphoto

def generateQuery(form):
	out = 'pstate='+form['state']
	if form['siteType'] != '':
		out += '&siteType=' + form['siteType']
	if form['Amenity'] != '':
		out += '&amenity=' + form['Amenity']
	return out

def homepage(request):
	if request.method == 'GET':
		ip_api_key = '97f4d203b989b3fe87045b255e7a29d42f403cafc8726c45172079dbaa60fbfe'
		ipinfo = pyipinfodb.IPInfo(ip_api_key)
		# ip = ipinfo.GetPublicIp()
		ip = '165.91.11.22'
		memcache.set('ip', ip)
		logging.error(ip)
		# use clients' public ip address to find their locations
		dataDict = memcache.get(ip)
		if dataDict is None:
			dataDict = ipinfo.GetCity(ip = ip)
			memcache.set(ip, dataDict)
		lat = dataDict["latitude"]
		lon = dataDict["longitude"]
		# logging.error(dataDict)
		API_KEY = 'AIzaSyAnEt9j1iiUDG6X2cRxQ2GUfotwoe4vCCY'
		google_maps = "https://maps.googleapis.com/maps/api/js?key="+API_KEY+"&sensor=false"
		content = {'google_maps_src': google_maps ,
		           'latitude' : float(lat),
		           'longitude' : float(lon)
		           }
		return render(request, 'mainpage/userform.html', content)

def submit(request):
	if request.method == 'POST':
		form = UserParkForm(request.POST)
		if form.is_valid():
			user_need = form.cleaned_data
			ip = memcache.get('ip')
			logging.error(ip)
			dataDict = memcache.get(ip)
			lat = dataDict["latitude"]
			lon = dataDict["longitude"]
			res = recommender.recommend(3, float(lat), float(lon))
			API_KEY = 'AIzaSyAnEt9j1iiUDG6X2cRxQ2GUfotwoe4vCCY'
			google_maps = "https://maps.googleapis.com/maps/api/js?key="+API_KEY+"&sensor=false"
			content = {'results': res,
					   'google_maps_src': google_maps ,
		               'latitude' : float(lat),
		               'longitude' : float(lon),
		               'lat1': float(res[0]['latitude']),
		               'lon1': float(res[0]['longitude']),
		               'lat2': float(res[1]['latitude']),
		               'lon2': float(res[1]['longitude']),
		               'lat3': float(res[2]['latitude']),
		               'lon3': float(res[2]['longitude'])}
			return render(request, 'mainpage/recommend.html', content)













