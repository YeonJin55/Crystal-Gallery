# Generated by Django 3.2.3 on 2021-07-20 10:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0019_auto_20210720_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='explain',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 7, 20, 10, 44, 51, 587194, tzinfo=utc), null=True),
        ),
    ]
