# Generated by Django 5.0.2 on 2024-03-06 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]