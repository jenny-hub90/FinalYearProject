# Generated by Django 3.2.3 on 2022-04-14 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HSC', '0029_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentimage', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('studentreview', models.TextField(max_length=800)),
                ('studentname', models.CharField(max_length=200)),
            ],
        ),
    ]
