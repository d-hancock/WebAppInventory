# Generated by Django 2.1.2 on 2018-11-05 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealership_name', models.CharField(max_length=50)),
                ('domain_assoc', models.CharField(max_length=50)),
                ('new_inventory_url', models.CharField(max_length=100)),
                ('used_inventory_url', models.CharField(max_length=100)),
                ('cpo_inventory_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=4)),
                ('make', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(max_length=20)),
                ('trim', models.CharField(max_length=30)),
                ('price', models.FloatField(max_length=15)),
                ('vin', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=40)),
                ('new_old', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleMsrpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4)),
                ('make', models.CharField(max_length=20)),
                ('vehicle_model', models.CharField(max_length=20)),
                ('msrp_high', models.FloatField(max_length=15)),
                ('msrp_low', models.FloatField(max_length=15)),
                ('full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Inventories')),
            ],
        ),
    ]
