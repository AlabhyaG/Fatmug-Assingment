# Generated by Django 5.0.6 on 2024-05-11 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_alter_vendormodel_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalPerformance',
            new_name='HistoricalPerformanceModel',
        ),
    ]