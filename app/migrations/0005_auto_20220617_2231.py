# Generated by Django 2.2.27 on 2022-06-17 13:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220617_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 22, 31, 49, 952759), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='discuss_borad',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 22, 31, 49, 950758), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='discuss_borad',
            name='product_code',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.product_code'),
        ),
        migrations.AlterField(
            model_name='product_borad',
            name='Create_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 17, 22, 31, 49, 950758), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='product_borad',
            name='product_code',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.product_code'),
        ),
        migrations.AlterField(
            model_name='product_image',
            name='product_code',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.product_code'),
        ),
    ]
