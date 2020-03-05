# Generated by Django 3.0.3 on 2020-03-05 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('file_upload', models.FileField(upload_to='Pictures/Gallery7/%Y')),
                ('description', models.TextField(blank=True)),
                ('upload_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Gallery 7',
            },
        ),
    ]