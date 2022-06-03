from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser
from rest_framework.decorators import parser_classes
from .models import prestasi
from datetime import date, datetime
from rest_framework.authtoken.models import Token
import json

def handle_uploaded_file(f):
    print(f)
    with open('img/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@api_view(['POST'])
def insertPrestasi(request):
    prestasiinsert = prestasi.objects.create(nama_event=request.data['nama_event'],
                                  url_kegiatan=request.data['url_kegiatan'],
                                  penyelenggara=request.data['penyelenggara'],
                                  lingkup_tingkat=request.data['lingkup_tingkat'],
                                  jumlah_negara=request.data['jumlah_negara'],
                                  kategori=request.data['kategori'],
                                  prestasi_diraih=request.data['prestasi_diraih'],
                                  ekuivalensi=request.data['ekuivalensi'],
                                  tempat=request.data['tempat'],
                                  tanggal_mulai=datetime.strptime(request.data['tanggal_mulai'], '%Y-%m-%d'),
                                  tanggal_selesai=datetime.strptime(request.data['tanggal_selesai'], '%Y-%m-%d'),
                                  deskripsi=request.data['deskripsi'],
                                  foto_kegiatan=request.data['foto_kegiatan'],
                                  bukti=request.data['bukti'],
                                  tim_individu=request.data['tim_individu'],
                                  jenis_prestasi=request.data['jenis_prestasi'])
    prestasiinsert.user.add(User.objects.get(username=Token.objects.get(key=request.data['token']).user).id)
    if request.data['tim_individu'] == 'tim':
        for value in json.loads(request.data['anggota']):
            print(value)
            prestasiinsert.user.add(User.objects.get(account__nim=value).id)
    handle_uploaded_file(request.data['foto_kegiatan'])
    handle_uploaded_file(request.data['bukti'])
    return Response()