#Django views are Python functions that takes http requests and returns http response, like HTML documents
#{} shows that there is nothing to pass init

from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {}) 

def about(request):
	return render(request, 'about.html', {})

def resume(request):
	return render(request, 'resume.html', {})

def portfolio(request):
	return render(request, 'portfolio.html', {})

def contact(request):
	return render(request, 'contact.html', {})