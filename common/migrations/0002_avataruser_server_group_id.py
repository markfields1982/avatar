# Generated by Django 3.0.4 on 2020-09-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avataruser',
            name='server_group_id',
            field=models.TextField(default='', max_length=500),
        ),
    ]
