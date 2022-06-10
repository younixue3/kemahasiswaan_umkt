from django.shortcuts import render
from prestasi_mahasiswa.models import prestasi, mahasiswa
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.db.models import Count
from rest_framework.response import Response
import random
from utils.helper import get_user_profiles, get_prodi

@api_view(['GET'])
def topChartGet(request):
    context = {'label': [], 'data': []}
    if request.method == 'GET':
        user = mahasiswa.objects.annotate(num_prestasi=Count('prestasi')).all()
        for value in user.order_by('-num_prestasi'):
            context['label'].append(get_user_profiles(value.nim)['nama'])
            context['data'].append(value.num_prestasi)
        return Response(context)

@api_view(['GET'])
def jenisChartGet(request):
    context = {'data': [{'label':'Penghargaan', 'data': [prestasi.objects.filter(jenis_prestasi='penghargaan').all().count()], 'backgroundColor': '#41B883' }, {'label':'Organisasi/Kepanitiaan', 'data': [prestasi.objects.filter(jenis_prestasi='organisasi').all().count()], 'backgroundColor': '#00D8FF' }, {'label':'Seminar/Workshop/Keahlian', 'data': [prestasi.objects.filter(jenis_prestasi='seminar').all().count()], 'backgroundColor': '#E46651' }]}
    if request.method == 'GET':
        return Response(context)

@api_view(['GET'])
def prodiChartGet(request):
    context = {'label': [], 'data': [], 'bgcolor': []}
    if request.method == 'GET':
        for value in get_prodi()['data']:
            context['label'].append(value['nama'])
            context['bgcolor'].append("#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]))
            nilai = 0
            for value in mahasiswa.objects.filter(prodi=value['idProdi']).annotate(num_prestasi=Count('prestasi')).all():
                nilai = nilai + value.num_prestasi
            context['data'].append(nilai)
        return Response(context)