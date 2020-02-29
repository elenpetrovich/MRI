# Generated by Django 2.1.7 on 2019-06-26 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0009_auto_20190615_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Директор'),
        ),
    ]