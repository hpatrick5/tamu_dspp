# Generated by Django 2.0.2 on 2021-04-18 06:36

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20210418_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='fname',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]