# Generated by Django 4.2.3 on 2023-07-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albuns', '0002_alter_album_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
