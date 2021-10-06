# Generated by Django 3.2.6 on 2021-09-30 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_adreess'),
        ('adminapp', '0002_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('payment_id', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.product')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.register')),
            ],
        ),
    ]
