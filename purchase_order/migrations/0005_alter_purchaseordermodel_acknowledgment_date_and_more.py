# Generated by Django 5.0.6 on 2024-05-11 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0004_purchaseordermodel_delivery_date'),
        ('vendor', '0004_alter_vendormodel_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='acknowledgment_date',
            field=models.DateTimeField(blank=True, help_text='Date when the purchase order was acknowledged.', null=True),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='delivery_date',
            field=models.DateTimeField(help_text='Expected delivery date for the purchase order.'),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Date when the purchase order was issued.'),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='items',
            field=models.JSONField(help_text='Details of the items in the purchase order.'),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='order_date',
            field=models.DateTimeField(help_text='Date when the purchase order was placed.'),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='po_number',
            field=models.CharField(help_text='Unique identifier for the purchase order.', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='quality_rating',
            field=models.FloatField(blank=True, help_text='Quality rating assigned to the purchase order.', null=True),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='quantity',
            field=models.PositiveIntegerField(help_text='Quantity of items in the purchase order.'),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='status',
            field=models.CharField(default='Pending', help_text='Current status of the purchase order.', max_length=20),
        ),
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='vendor',
            field=models.ForeignKey(help_text='Related vendor for the purchase order.', on_delete=django.db.models.deletion.CASCADE, to='vendor.vendormodel'),
        ),
    ]