# Generated by Django 4.0.2 on 2022-06-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestasi_mahasiswa', '0004_alter_prestasi_bukti_alter_prestasi_foto_kegiatan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestasi',
            name='tanggal_mulai',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='prestasi',
            name='tanggal_selesai',
            field=models.DateTimeField(),
        ),
    ]
