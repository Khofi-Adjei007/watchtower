# Generated by Django 5.0.4 on 2024-04-13 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_practice_data_first_name_practice_data_last_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='practice_data',
            new_name='registrations',
        ),
    ]
