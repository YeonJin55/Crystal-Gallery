# Generated by Django 3.2.3 on 2021-08-05 15:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0033_auto_20210806_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='time_ending',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 15, 45, 34, 704332, tzinfo=utc), null=True),
        ),
    ]
