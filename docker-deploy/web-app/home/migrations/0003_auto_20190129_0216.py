# Generated by Django 2.1.5 on 2019-01-29 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190129_0148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user1',
            new_name='user',
        ),
    ]
