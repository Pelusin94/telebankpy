# Generated by Django 2.1.15 on 2020-07-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charitynames',
            name='display_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
