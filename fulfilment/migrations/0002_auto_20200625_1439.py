# Generated by Django 2.1.15 on 2020-06-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='upload_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='user_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
