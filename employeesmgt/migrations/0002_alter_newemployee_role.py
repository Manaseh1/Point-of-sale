# Generated by Django 3.2 on 2023-07-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeesmgt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newemployee',
            name='role',
            field=models.CharField(choices=[('manager', 'manager'), ('employee', 'employee')], max_length=100),
        ),
    ]