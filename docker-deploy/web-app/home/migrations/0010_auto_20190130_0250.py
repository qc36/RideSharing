# Generated by Django 2.1.5 on 2019-01-30 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190130_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='owner',
        ),
        migrations.AddField(
            model_name='owner',
            name='order',
            field=models.ManyToManyField(null=True, related_name='owner', to='home.Order'),
        ),
    ]
