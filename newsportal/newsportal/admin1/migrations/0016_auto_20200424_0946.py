# Generated by Django 3.0.2 on 2020-04-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0015_extended_user_is_blocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extended_user',
            name='is_login',
            field=models.CharField(default='', max_length=50),
        ),
    ]