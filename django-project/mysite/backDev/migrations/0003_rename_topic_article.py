# Generated by Django 4.1.2 on 2024-12-16 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backDev', '0002_topic_delete_article'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Article',
        ),
    ]
