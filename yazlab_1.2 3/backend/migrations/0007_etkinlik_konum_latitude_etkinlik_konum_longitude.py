# Generated by Django 5.1.3 on 2024-11-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_rename_etkinlik_suresi_etkinlik_sure'),
    ]

    operations = [
        migrations.AddField(
            model_name='etkinlik',
            name='konum_latitude',
            field=models.FloatField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='konum_longitude',
            field=models.FloatField(default=3),
            preserve_default=False,
        ),
    ]