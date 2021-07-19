# Generated by Django 3.2.2 on 2021-07-19 03:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0010_auto_20210719_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='coin',
            field=models.IntegerField(default=9999),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 7, 19, 3, 12, 48, 476869, tzinfo=utc), null=True),
        ),
    ]
