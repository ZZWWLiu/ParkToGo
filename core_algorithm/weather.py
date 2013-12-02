import json
import urllib2

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

def processWeatherData(data):
	result = []
	for day in data['list']:
		main_info = {'weather' : day['weather'][0], 'temp': day['temp']}
		result.append(main_info)
	return result

