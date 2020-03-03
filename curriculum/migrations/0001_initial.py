# Generated by Django 3.0.3 on 2020-03-03 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('crew', models.CharField(blank=True, max_length=5000, verbose_name='Available Teachers')),
                ('follow_up_by', models.CharField(blank=True, max_length=5000)),
                ('period_tought', models.CharField(blank=True, max_length=5000)),
                ('description', models.TextField()),
                ('possision', models.CharField(blank=True, choices=[('400ms', '400ms'), ('500ms', '500ms'), ('600ms', '600ms'), ('700ms', '700ms')], default='400ms', max_length=10)),
                ('edit_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Curriculum',
            },
        ),
    ]
