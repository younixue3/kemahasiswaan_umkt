# Generated by Django 4.0.3 on 2022-06-10 01:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_uniid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uniid',
            field=models.UUIDField(default=uuid.UUID('7735de6e-fcd5-4de7-8e3c-b537f4f1f64d'), editable=False),
        ),
    ]
