from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
import json
from products.models import *
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# -----------------------------------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------------------------------



# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     instance = Products.objects.all()
#     data ={}
#     if instance:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         #data = model_to_dict(instance)
#         data_ser  = ProductSerializer(instance, many=True).data
#     return Response(data_ser)

# -----------------------------------------------------------------------------------------------------


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    print(request.data)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response({'invalid':'not a valid data'})