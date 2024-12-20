# Generated by Django 5.1.3 on 2024-11-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_etkinlik_konum_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etkinlik',
            name='konum_latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='etkinlik',
            name='konum_longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='etkinlik',
            name='sure',
            field=models.IntegerField(default=0),
        ),
    ]
