# Generated by Django 4.1.6 on 2023-02-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.URLField(max_length=255)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]