# Generated by Django 4.2.3 on 2023-07-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albuns', '0003_album_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
