# Generated by Django 2.1.15 on 2020-07-30 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0009_auto_20200730_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fulfilmentfilesdata',
            name='file_name',
        ),
    ]
