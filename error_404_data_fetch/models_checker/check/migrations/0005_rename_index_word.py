# Generated by Django 4.2.7 on 2023-12-26 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_alter_index_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='index',
            new_name='Word',
        ),
    ]
