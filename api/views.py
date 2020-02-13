from django.shortcuts import render, HttpResponse


# Create your views here.

def get_data(request):
    print(request.GET)
    print(request.POST)

    return HttpResponse('OK')
