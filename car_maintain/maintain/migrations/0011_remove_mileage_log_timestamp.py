# Generated by Django 3.1.3 on 2020-12-11 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintain', '0010_mileage_log_timestamp_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mileage_log',
            name='timestamp',
        ),
    ]