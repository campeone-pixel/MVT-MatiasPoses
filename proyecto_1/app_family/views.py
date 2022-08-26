from django.shortcuts import render
from .models import familiar
from django.http import HttpResponse
from django.template import loader



def hermano(request):
  familiar1=familiar(nombre='Gabriel',relacion="hermano", nacimiento='2001-01-21', edad=23)
  familiar1.save()
  plantilla=loader.get_template("template1.html")
 
  diccionario={'nombre':familiar1.nombre ,'relacion':familiar1.relacion ,'nacimiento': familiar1.nacimiento, 'edad':familiar1.edad }
  
  documento=plantilla.render(diccionario)
  return HttpResponse(documento)

def hermana(request):
  familiar1=familiar(nombre='Noelia',relacion="hermana", nacimiento='1991-04-29', edad=31)
  diccionario={'nombre':familiar1.nombre ,'relacion':familiar1.relacion ,'nacimiento': familiar1.nacimiento, 'edad':familiar1.edad }

  familiar1.save()
  
  plantilla=loader.get_template("template1.html")
 
  documento=plantilla.render(diccionario)
  return HttpResponse(documento)

def madre(request):
  familiar1=familiar(nombre='Mirta',relacion="madre", nacimiento='1967-12-31', edad=55)
  diccionario={'nombre':familiar1.nombre ,'relacion':familiar1.relacion ,'nacimiento': familiar1.nacimiento, 'edad':familiar1.edad }
  familiar1.save()
  plantilla=loader.get_template("template1.html")
 
  documento=plantilla.render(diccionario)
  return HttpResponse(documento)

def padre(request):
  familiar1=familiar(nombre='Claudio',relacion="padre", nacimiento='1968-06-19', edad=54)
  diccionario={'nombre':familiar1.nombre ,'relacion':familiar1.relacion ,'nacimiento': familiar1.nacimiento, 'edad':familiar1.edad }
  familiar1.save()
  plantilla=loader.get_template("template1.html")
 
  documento=plantilla.render(diccionario)
  return HttpResponse(documento)