# Generated by Django 2.0 on 2018-11-19 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_auto_20181118_0621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='metadescription',
        ),
    ]