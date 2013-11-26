# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from mainpage.models import UserParkForm
import urllib2
from xml.dom import minidom
# from django.core.cache import cache
import logging
# import re
# import hashlib

def homepage(request):
	if request.method == 'GET':
		return render(request, 'mainpage/userform.html')
		# return render(request, 'mainpage/left-sidebar.html')
	

def submit(request):
	if request.method == 'POST':
		form = UserParkForm(request.POST)
		if form.is_valid():
			user_need = form.cleaned_data
			logging.error(user_need)
			state = 'pstate='+user_need['state']
			siteType = '&siteType=' + user_need['siteType']
			Amenity = '&amenity=' + user_need['Amenity']
			api = 'http://api.amp.active.com/camping/campgrounds?'+state+siteType+Amenity+'&expwith=1&pets=3010&arvdate=05/15/2014&lengthOfStay=5&api_key=2chxq68efd4azrpygt5hh2qu'
			logging.error(api)
			urlfile = urllib2.urlopen(api)
			data = urlfile.read()
			# logging.error(res)
			urlfile.close()
			# parse the xml
			dom = minidom.parseString(data)
			resultlist = dom.getElementsByTagName('result')
			facilityIDlist = []
			contractTypelist = []
			facilityNamelist = []
			# we only cares about the state parks (others do not have a detail info)
			for s in resultlist:
				if s.attributes['contractType'].value == 'STATE':
					facilityIDlist.append(s.attributes['facilityID'].value)
					facilityNamelist.append(s.attributes['facilityName'].value)
				# contractTypelist.append(s.attributes['contractType'].value)
			cont = {'facilityID': facilityIDlist,
			        # 'contractType': contractTypelist,
			        'facilityName': facilityNamelist}

			return render(request, 'mainpage/recommend.html', cont)
