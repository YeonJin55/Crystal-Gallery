# Generated by Django 3.2.2 on 2021-08-07 02:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0037_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='time_ending',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 8, 7, 2, 23, 18, 300721, tzinfo=utc), null=True),
        ),
    ]