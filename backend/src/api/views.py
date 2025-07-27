from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_view(request, *agrs, **kwargs):
    data = {
        'name': "donald",
        'language' : 'python',
    }

    return JsonResponse(data)
