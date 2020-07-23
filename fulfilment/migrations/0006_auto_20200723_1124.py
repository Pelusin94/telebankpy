# Generated by Django 2.1.15 on 2020-07-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0005_uploadfile_file_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fulfilmenttype',
            old_name='file_type',
            new_name='display_type',
        ),
        migrations.RenameField(
            model_name='uploadfile',
            old_name='file_type',
            new_name='system_type',
        ),
        migrations.AddField(
            model_name='fulfilmenttype',
            name='system_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]