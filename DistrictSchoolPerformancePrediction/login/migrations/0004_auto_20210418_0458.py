# Generated by Django 2.0.2 on 2021-04-18 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210418_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='fname',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
