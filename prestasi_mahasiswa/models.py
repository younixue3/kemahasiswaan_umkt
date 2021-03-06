from django.db import models
from django.contrib.auth.models import User

class mahasiswa(models.Model):
    nim = models.CharField(max_length=20)
    prodi = models.CharField(max_length=20)

class prestasi(models.Model):
    TIM = 'tim'
    INDIVIDU = 'individu'
    TIM_INDIVIDU_CHOICES = [
        (TIM, 'Tim'),
        (INDIVIDU, 'Individu'),
    ]
    PENGHARGAAN = 'penghargaan'
    SEMINAR = 'seminar'
    ORGANISASI = 'organisasi'
    JENIS_PRESTASI_CHOICES = [
        (PENGHARGAAN, 'penghargaan'),
        (SEMINAR, 'seminar'),
        (ORGANISASI, 'organisasi'),
    ]
    nama_event = models.CharField(max_length=80)
    url_kegiatan = models.TextField()
    penyelenggara = models.CharField(max_length=80)
    lingkup_tingkat = models.CharField(max_length=50)
    jumlah_negara = models.IntegerField()
    kategori = models.CharField(max_length=50)
    prestasi_diraih = models.CharField(max_length=80)
    ekuivalensi = models.CharField(max_length=80)
    tempat = models.TextField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    deskripsi = models.TextField()
    bukti = models.FileField(upload_to='img/')
    foto_kegiatan = models.FileField(upload_to='img/')
    tim_individu = models.CharField(
        max_length=10,
        choices=TIM_INDIVIDU_CHOICES,
        default=INDIVIDU
    )
    jenis_prestasi = models.CharField(
        max_length=20,
        choices=JENIS_PRESTASI_CHOICES
    )
    mahasiswa = models.ManyToManyField(mahasiswa)
