# Generated by Django 3.2 on 2023-07-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0003_auto_20230710_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='totals',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
