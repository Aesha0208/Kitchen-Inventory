# Generated by Django 3.2.24 on 2024-03-20 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_add_inventory_unit_of_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_inventory',
            old_name='Unit_Of_Product',
            new_name='Unit',
        ),
    ]
