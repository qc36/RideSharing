# Generated by Django 2.1.5 on 2019-01-30 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190130_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='last_name',
        ),
    ]