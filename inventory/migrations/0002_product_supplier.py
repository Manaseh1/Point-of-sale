# Generated by Django 3.2 on 2023-06-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.CharField(default=None, max_length=100),
        ),
    ]