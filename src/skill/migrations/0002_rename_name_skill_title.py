# Generated by Django 4.0.1 on 2022-01-10 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='name',
            new_name='title',
        ),
    ]
