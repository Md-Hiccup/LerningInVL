# Generated by Django 2.0.4 on 2018-04-16 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_auto_20180416_1028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
