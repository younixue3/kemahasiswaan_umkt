# Generated by Django 4.0.2 on 2022-05-31 21:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='prestasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_event', models.CharField(max_length=80)),
                ('url_kegiatan', models.TextField()),
                ('penyelenggara', models.CharField(max_length=80)),
                ('lingkup_tingkat', models.CharField(max_length=50)),
                ('jumlah_negara', models.IntegerField()),
                ('kategori', models.CharField(max_length=50)),
                ('prestasi_diraih', models.CharField(max_length=80)),
                ('ekuivalensi', models.CharField(max_length=80)),
                ('tempat', models.TextField()),
                ('tanggal_mulai', models.DateField()),
                ('tanggal_selesai', models.DateField()),
                ('deskripsi', models.TextField()),
                ('bukti', models.TextField()),
                ('foto_kegiatan', models.TextField()),
                ('tim_individu', models.CharField(choices=[('tim', 'Tim'), ('individu', 'Individu')], default='individu', max_length=10)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
