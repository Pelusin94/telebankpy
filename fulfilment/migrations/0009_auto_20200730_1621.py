# Generated by Django 2.1.15 on 2020-07-30 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fulfilment', '0008_fulfilmentfilesdata_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fulfilmentfilesdata',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
