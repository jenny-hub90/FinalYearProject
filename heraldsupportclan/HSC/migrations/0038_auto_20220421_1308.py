# Generated by Django 3.2.3 on 2022-04-21 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HSC', '0037_notification_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_detail', models.TextField()),
                ('status', models.BooleanField()),
                ('ready_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HSC.author')),
            ],
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
