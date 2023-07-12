# Generated by Django 3.2 on 2023-07-12 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=100)),
                ('product_name', models.CharField(default=None, max_length=100)),
                ('quantity', models.FloatField(default=0)),
                ('unit_price', models.FloatField(default=0)),
                ('totals', models.FloatField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dummy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
        ),
    ]
