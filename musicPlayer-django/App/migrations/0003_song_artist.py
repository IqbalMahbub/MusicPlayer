# Generated by Django 2.2.4 on 2021-01-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_song_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.TextField(default='andre'),
            preserve_default=False,
        ),
    ]
