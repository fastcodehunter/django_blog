# Generated by Django 5.0.2 on 2024-02-29 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_news_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_news',
            name='preview',
            field=models.ImageField(upload_to='blog_previews/'),
        ),
    ]
