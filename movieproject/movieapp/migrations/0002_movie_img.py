# Generated by Django 4.0.6 on 2022-11-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='sdss', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
