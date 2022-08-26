from django.http import HttpResponse
from django.template import loader


def probando_html(request):
  nom="gabriel"
  rel='hermano'
  edad='22'
  diccionario= {'nombre':nom, 'relacion':rel, "edad":edad}
  plantilla=loader.get_template("template1.html")
 
  documento=plantilla.render(diccionario)
  return HttpResponse(documento)
  
