# Generated by Django 5.0.2 on 2024-03-04 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_news_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog_news',
            options={},
        ),
        migrations.AlterField(
            model_name='subsection',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]