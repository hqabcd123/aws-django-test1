# Generated by Django 2.2.27 on 2022-06-03 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220604_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 2, 23, 53, 130443), help_text='create date: '),
        ),
    ]