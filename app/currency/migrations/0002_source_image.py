# Generated by Django 4.1.6 on 2023-04-02 11:26

import currency.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='image',
            field=models.FileField(blank=True, default='/static/av.png', null=True,
                                   upload_to=currency.models.source_image_path),
        ),
    ]