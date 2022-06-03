from django.shortcuts import render
from prestasi_mahasiswa.models import prestasi
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.db.models import Count
from rest_framework.response import Response

@api_view(['GET'])
def topChartGet(request):
    context = {'label': [], 'data': []}
    if request.method == 'GET':
        user = User.objects.annotate(num_prestasi=Count('prestasi')).all()
        for value in user.order_by('-num_prestasi'):
            context['label'].append(value.first_name + ' ' + value.last_name,)
            context['data'].append(value.num_prestasi)
        return Response(context)

@api_view(['GET'])
def jenisChartGet(request):
    context = {'data': [{'label':'Penghargaan', 'data': [prestasi.objects.filter(jenis_prestasi='penghargaan').all().count()], 'backgroundColor': '#41B883' }, {'label':'Organisasi/Kepanitiaan', 'data': [prestasi.objects.filter(jenis_prestasi='organisasi').all().count()], 'backgroundColor': '#00D8FF' }, {'label':'Seminar/Workshop/Keahlian', 'data': [prestasi.objects.filter(jenis_prestasi='seminar').all().count()], 'backgroundColor': '#E46651' }]}
    if request.method == 'GET':
        return Response(context)