# Generated by Django 3.2.24 on 2024-03-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=200)),
                ('Quantity', models.CharField(max_length=200)),
            ],
        ),
    ]
