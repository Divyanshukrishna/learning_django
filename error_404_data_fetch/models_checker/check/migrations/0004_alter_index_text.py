# Generated by Django 4.2.7 on 2023-12-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_alter_index_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]