# Generated by Django 3.2.6 on 2021-09-16 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_email', models.EmailField(max_length=254)),
                ('usr_passw', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_name', models.CharField(max_length=150)),
                ('usr_gender', models.IntegerField(max_length=2)),
                ('usr_phone', models.CharField(max_length=150)),
                ('usr_loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.login')),
            ],
        ),
    ]
