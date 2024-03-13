# Generated by Django 5.0.2 on 2024-03-12 19:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('director', models.CharField(max_length=255, verbose_name='Director name')),
                ('rating', models.FloatField(verbose_name='Rating')),
                ('description', models.TextField(verbose_name='Description')),
                ('url_poster', models.CharField(max_length=500, verbose_name='URL Poster')),
                ('url_banner', models.CharField(max_length=500, verbose_name='URL Banner')),
                ('url_movie', models.CharField(max_length=500, verbose_name='URL Movie')),
                ('is_top_ten', models.BooleanField(blank=True, null=True, verbose_name='Is top 10')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CD_app.genre', verbose_name='Genre')),
            ],
        ),
    ]
