# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_cover',
            field=models.FileField(upload_to=''),
        ),
    ]
