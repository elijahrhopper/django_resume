# Generated by Django 4.0.1 on 2022-01-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_rename_name_skill_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.CharField(choices=[('expert', 'EXPERT'), ('beginner', 'BEGINNER'), ('intermediate', 'INTERMEDIATE')], default='intermediate', max_length=15),
        ),
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
