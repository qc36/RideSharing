# Generated by Django 2.1.5 on 2019-02-06 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20190206_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-aptime'], 'permissions': (('confirm_order', 'Can change order status'), ('change_order_info', 'Can change order information'), ('create_order', 'Can create'))},
        ),
    ]
