# Generated by Django 4.1.6 on 2023-04-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=11, max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False,
                                      help_text='Designates that this user has all '
                                                'permissions without explicitly assigning them.',
                                      verbose_name='superuser status'),
        ),
    ]
