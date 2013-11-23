# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect

# from django.core.cache import cache
import logging
# import re
# import hashlib

def homepage(request):
	# return render(request, 'mainpage/homepage.html')
	return render(request, 'mainpage/left-sidebar.html')