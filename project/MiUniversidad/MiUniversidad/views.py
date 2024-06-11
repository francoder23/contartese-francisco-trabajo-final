from django.http import HttpResponse
from django.template import Context,Template


def saludar(request):
    return HttpResponse("Bienvenido a la universidad")
 
def segunda_vista(request):
    return HttpResponse("<h1> Universidad de finanzas </h1>")

def nombre(request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre},")
    
def probando_template(request):
    mi_html = open("./templates/templates1.html", encoding="UTF-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context({"saludo":"!Bienvenido!",})
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)
    