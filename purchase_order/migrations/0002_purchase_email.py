# Generated by Django 3.2 on 2023-07-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]