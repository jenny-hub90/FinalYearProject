# Generated by Django 3.2.3 on 2022-02-23 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HSC', '0014_eventreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toppost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstitle', models.CharField(max_length=255)),
                ('newsimage', models.ImageField(max_length=800, upload_to='eventstudentsreview/')),
                ('newsdesc', models.TextField(max_length=800)),
            ],
        ),
    ]
