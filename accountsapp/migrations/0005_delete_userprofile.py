# Generated by Django 3.2.6 on 2022-01-09 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_delete_chef'),
        ('accountsapp', '0004_auto_20220108_2031'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
