# Generated by Django 3.2.13 on 2023-05-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.TextField(blank=True, null=True),
        ),
    ]
