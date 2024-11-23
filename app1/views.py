from django.http import  HttpResponse

def greet(request):
    return HttpResponse("Hii This is my first Project..!")