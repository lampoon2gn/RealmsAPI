# Generated by Django 3.1 on 2020-08-13 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RealmsEmail', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='ClientMsg',
        ),
    ]
