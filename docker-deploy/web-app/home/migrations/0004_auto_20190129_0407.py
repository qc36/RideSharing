# Generated by Django 2.1.5 on 2019-01-29 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_auto_20190129_0216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={},
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='email',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='number',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='email',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='number',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='name',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='name',
        ),
        migrations.AddField(
            model_name='driver',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='user',
            field=models.ForeignKey(default=233, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='user',
            field=models.ForeignKey(default=233, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
