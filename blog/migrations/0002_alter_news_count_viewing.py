# Generated by Django 5.0.2 on 2024-03-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='count_viewing',
            field=models.ManyToManyField(blank=True, related_name='view_count', to='profil.profil'),
        ),
    ]
