# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from mainpage.models import UserParkForm
import urllib2
from xml.dom import minidom
# from django.core.cache import cache
import logging
# import re
# import hashlib

def generateQuery(form):
	out = 'pstate='+form['state']
	if form['siteType'] != '':
		out += '&siteType=' + form['siteType']
	if form['Amenity'] != '':
		out += '&amenity=' + form['Amenity']
	return out

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
			query = generateQuery(user_need)
			camp_search = 'http://api.amp.active.com/camping/campgrounds?'+query+'&expwith=1&pets=3010&arvdate=05/15/2014&lengthOfStay=5&api_key=2chxq68efd4azrpygt5hh2qu'
			logging.error(camp_search)
			urlfile = urllib2.urlopen(camp_search)
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
			camp_detail = 'http://api.amp.active.com/camping/campground/details?contractCode=CO&parkId=50032&api_key=2chxq68efd4azrpygt5hh2qu'
			return render(request, 'mainpage/recommend.html', cont)
