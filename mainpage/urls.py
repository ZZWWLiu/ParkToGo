from django.conf.urls import patterns, url

from mainpage import views

urlpatterns = patterns('',
	# ex: /parktogo/
	url(r'^$', views.homepage, name = 'homepage'),
    # ex: /parktogo/submit
	url(r'^submit', views.submit, name = 'submit'),
)