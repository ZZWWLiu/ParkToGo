import json
# import urllib2
from google.appengine.api import urlfetch

def weatherForcast(lat, lon):
	"""OpenWeatherMap API
	   Input: lat and lon String
	   Output: dict of weather info
	"""
	api_key = '9f282f36bbd552d28d07769dcb3e7019'
	query = '&lat='+lat+'&lon='+lon+'&APPID='+api_key
	Url = 'http://api.openweathermap.org/data/2.5/forecast/daily?cnt=10&mode=json'+query
	result = urlfetch.fetch(Url)
	if result.status_code == 200:
		data = result.content
		datadict = json.loads(data)
		return datadict
	else:
		return None

def toFahrenheit(kelvin):
	return kelvin*9/5 - 459.67

def processWeatherData(data):
	result = []
	for day in data['list']:
		for key in day['temp']:
			day['temp'][key] = toFahrenheit(day['temp'][key])
		main_info = {'weather' : day['weather'][0], 'temp': day['temp']}
		result.append(main_info)
	return result


def getWeather(lat, lon):
	data = weatherForcast(lat, lon)
	if data :
		return processWeatherData(data)
	else:
		return None