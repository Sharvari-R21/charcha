# Generated by Django 2.1.4 on 2018-12-30 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20181230_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channelmember',
            name='role',
        ),
    ]
