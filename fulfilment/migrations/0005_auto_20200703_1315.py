# Generated by Django 2.1.15 on 2020-07-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0004_downloadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadfile',
            name='merge_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]