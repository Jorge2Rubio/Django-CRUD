# Generated by Django 5.0.2 on 2024-04-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictweb', '0002_alter_students_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]