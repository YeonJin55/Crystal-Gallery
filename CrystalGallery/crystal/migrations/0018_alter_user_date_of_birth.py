# Generated by Django 3.2.3 on 2021-07-20 00:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0017_alter_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 7, 20, 0, 43, 56, 81229, tzinfo=utc), null=True),
        ),
    ]
