from django.conf.urls import patterns, url

from mainpage import views

urlpatterns = patterns('',
	# ex: /ParkToGo/
	url(r'^$', views.homepage, name = 'homepage'),
)