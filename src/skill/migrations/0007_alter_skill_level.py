# Generated by Django 4.0.1 on 2022-01-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0006_alter_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(choices=[('intermediate', 'INTERMEDIATE'), ('expert', 'EXPERT'), ('beginner', 'BEGINNER')], default='intermediate', max_length=15),
        ),
    ]