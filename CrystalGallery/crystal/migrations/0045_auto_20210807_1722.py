# Generated by Django 3.2.2 on 2021-08-07 08:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0044_auto_20210807_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='time_starting',
        ),
        migrations.AlterField(
            model_name='listing',
            name='time_ending',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 8, 7, 8, 22, 30, 538092, tzinfo=utc), null=True),
        ),
    ]