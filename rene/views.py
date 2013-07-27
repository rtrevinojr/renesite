
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render


# Create your views here.

def index(request) :
	template = loader.get_template( 'rene/home.html')
	robj = 'rene'
	context = RequestContext(request, {})	
	return HttpResponse(template.render(context))
	#return render(request, 'rene/home.html', {})
	#return HttpResponse("The rene trevino site")

def bio(request) :
	template = loader.get_template('rene/bio.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))


