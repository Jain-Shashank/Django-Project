# Generated by Django 3.2.6 on 2021-08-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0023_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
