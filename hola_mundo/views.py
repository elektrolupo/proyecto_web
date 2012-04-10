from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola mundo con Django 1.4")
