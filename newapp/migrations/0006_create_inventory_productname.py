# Generated by Django 3.2.24 on 2024-03-22 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_auto_20240322_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_inventory',
            name='ProductName',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='newapp.add_inventory'),
            preserve_default=False,
        ),
    ]