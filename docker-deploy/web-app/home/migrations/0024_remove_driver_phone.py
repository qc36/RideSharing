# Generated by Django 2.1.5 on 2019-02-05 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_order_passenger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='phone',
        ),
    ]
