from typing import DefaultDict
from django.db import models

LEVEL_CHOICES = {
    ('beginner', 'BEGINNER'),
    ('intermediate', 'INTERMEDIATE'),
    ('expert', 'EXPERT'),
}

TYPE_CHOICES = {
    ('experience', 'EXPERIENCE'),
    ('education', 'EDUCATION'),
    ('skill', 'SKILL'),
    ('project', 'PROJECT'),
}

# Create your models here.
class Skill(models.Model):
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, default='intermediate')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='experience')

    def __str__(self):
        return self.title