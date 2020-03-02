# Generated by Django 3.0.3 on 2020-02-28 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='about/administration/%Y')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('speach', models.TextField(blank=True, null=True)),
                ('possision', models.CharField(blank=True, max_length=100)),
                ('history', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
    ]
