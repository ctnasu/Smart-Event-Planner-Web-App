# Generated by Django 5.1.3 on 2024-11-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_kullanici_date_joined_kullanici_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etkinlik',
            name='sure',
        ),
        migrations.AddField(
            model_name='etkinlik',
            name='etkinlik_suresi',
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
    ]
