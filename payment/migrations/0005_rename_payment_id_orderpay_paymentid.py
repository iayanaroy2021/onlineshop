# Generated by Django 3.2.6 on 2021-10-04 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_orderpay'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderpay',
            old_name='payment_id',
            new_name='paymentid',
        ),
    ]
