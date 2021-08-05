# Generated by Django 3.2.3 on 2021-08-05 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0027_merge_0024_auto_20210727_0017_0026_auto_20210722_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='explain',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 10, 53, 2, 665057, tzinfo=utc), null=True),
        ),
    ]
