# Generated by Django 4.1 on 2024-12-28 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backDev', '0005_topskills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topskills',
            name='image',
            field=models.ImageField(upload_to='top_skills_img/'),
        ),
    ]
