# Generated by Django 4.2.8 on 2024-03-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_portalusers_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='practice_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('staff_id', models.CharField(max_length=14)),
                ('report_details', models.CharField(max_length=20)),
            ],
        ),
    ]