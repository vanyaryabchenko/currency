from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='source',
            field=models.CharField(default='test', max_length=25),
            preserve_default=False,
        ),
    ]
