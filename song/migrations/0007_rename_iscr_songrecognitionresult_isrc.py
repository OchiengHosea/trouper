# Generated by Django 4.0.3 on 2022-03-12 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0006_remove_songrecognitionresult_albums_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songrecognitionresult',
            old_name='iscr',
            new_name='isrc',
        ),
    ]
