from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.decorators import parser_classes
import base64, pdb

@api_view(['POST'])
def insertPrestasi(request):
    print(request.data)
    return Response(request.data)