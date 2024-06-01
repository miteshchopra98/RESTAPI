from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
import json
from products.models import *
from django.forms.models import model_to_dict


# Create your views here.

# def api_home(request, *args, **kwargs):
#     #print(dict(request.GET))
#     #print(dict(request.headers))
#     body  = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
    
#     print()

#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     print(data)
    
#     return JsonResponse({"message": "Hi there, this is your Django API response"})


def api_home(request, *args, **kwargs):
    model_data = Products.objects.all().order_by("?").first()
    data ={}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data)
    return JsonResponse(data)

