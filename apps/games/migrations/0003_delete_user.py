# Generated by Django 4.2.5 on 2023-09-19 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]