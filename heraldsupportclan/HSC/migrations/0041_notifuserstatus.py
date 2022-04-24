# Generated by Django 3.2.3 on 2022-04-22 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HSC', '0040_auto_20220421_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotifUserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('notif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HSC.notify')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]