from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def About(request):
	return render(request, 'About.html')

def Projects(request):
	return render(request, 'Projects.html')

def Contact(request):
	return render(request, 'Contact.html')

def Vault(request):
	return render(request, 'vault.html')

def Netapp(request):
	return render(request, 'netapp.html')

def CRUD(request):
	return render(request, 'CRUD.html')