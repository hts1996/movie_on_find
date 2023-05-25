# Generated by Django 3.2.13 on 2023-05-24 23:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('popularity', models.TextField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('release_date', models.CharField(blank=True, max_length=500, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=500, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=500, null=True)),
                ('video', models.TextField(blank=True, null=True)),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('interest', models.ManyToManyField(related_name='interest_movies', to=settings.AUTH_USER_MODEL)),
                ('watched', models.ManyToManyField(related_name='watched_movies', to=settings.AUTH_USER_MODEL)),
                ('watching', models.ManyToManyField(related_name='watching_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
