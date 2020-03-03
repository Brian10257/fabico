# Generated by Django 3.0.3 on 2020-02-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]