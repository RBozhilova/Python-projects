# Generated by Django 4.0.3 on 2022-03-18 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pesni4ki', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songs',
            old_name='song_gernes',
            new_name='song_genre',
        ),
    ]