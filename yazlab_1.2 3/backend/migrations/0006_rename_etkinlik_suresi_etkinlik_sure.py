# Generated by Django 5.1.3 on 2024-11-27 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_etkinlik_konum_lat_remove_etkinlik_konum_lng'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etkinlik',
            old_name='etkinlik_suresi',
            new_name='sure',
        ),
    ]