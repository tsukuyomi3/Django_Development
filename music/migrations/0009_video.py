# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_song_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('is_favorite', models.BooleanField(default=False)),
                ('video', models.FileField(max_length=500, upload_to='')),
                ('album', models.ForeignKey(default='Mugen', on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]