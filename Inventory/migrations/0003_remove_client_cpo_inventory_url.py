# Generated by Django 2.1.2 on 2018-11-05 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_auto_20181105_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='cpo_inventory_url',
        ),
    ]
