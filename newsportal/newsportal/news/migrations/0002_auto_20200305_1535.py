# Generated by Django 3.0.2 on 2020-03-05 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
        migrations.RemoveField(
            model_name='news_status',
            name='news_id',
        ),
        migrations.RemoveField(
            model_name='news_status',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='News_content',
        ),
        migrations.DeleteModel(
            name='News_Status',
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]