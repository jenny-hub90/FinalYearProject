# Generated by Django 3.2.3 on 2022-04-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HSC', '0026_remove_review_studentimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to='students/'),
        ),
    ]
