# Generated by Django 3.2.2 on 2021-06-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='explain',
            field=models.TextField(default=''),
        ),
    ]
