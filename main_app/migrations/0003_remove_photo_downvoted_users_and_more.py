# Generated by Django 5.0.1 on 2024-01-21 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_post_image_remove_post_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='downvoted_users',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='upvoted_users',
        ),
    ]