# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 05:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_fav'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_fav',
        ),
    ]
