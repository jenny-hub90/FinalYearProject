# Generated by Django 3.2.3 on 2022-04-21 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HSC', '0038_auto_20220421_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notify',
            old_name='ready_by',
            new_name='ready_by_Author',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='status',
        ),
        migrations.AddField(
            model_name='notify',
            name='ready_by_User',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
