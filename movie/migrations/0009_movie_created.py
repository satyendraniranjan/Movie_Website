# Generated by Django 2.2.4 on 2019-08-31 21:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 31, 21, 43, 59, 581117, tzinfo=utc)),
        ),
    ]