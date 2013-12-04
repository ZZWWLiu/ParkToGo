from datetime import date, timedelta

from django import template
register = template.Library()

@register.filter
def getDate(i):
	t = date.today()
	delta = timedelta(days = 1)
	day = t + int(i)*delta
	return day.strftime("%b %d")