# Generated by Django 2.2.4 on 2019-08-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20190830_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]