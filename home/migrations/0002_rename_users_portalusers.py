# Generated by Django 4.2.8 on 2024-03-28 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='portalUsers',
        ),
    ]