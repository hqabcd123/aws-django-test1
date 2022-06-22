# Generated by Django 2.2.27 on 2022-06-22 12:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220621_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='diagram',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 21, 29, 20, 785245), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='discuss_borad',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 21, 29, 20, 782244), help_text='create date: '),
        ),
        migrations.AlterField(
            model_name='product_borad',
            name='Create_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 21, 29, 20, 782244), help_text='create date: '),
        ),
        migrations.CreateModel(
            name='user_history_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodprint_set', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.user_history')),
            ],
        ),
        migrations.AddField(
            model_name='user_history',
            name='foodprint',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.product_borad'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('history', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='app.user_history_set')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]