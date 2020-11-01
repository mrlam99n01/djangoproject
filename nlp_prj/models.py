from django.db import models
COLOR_CHOICES = (
    ('Naive','NAIVE'),
    ('SVM', 'SVM'),
)
class Article(models.Model):
    title = models.CharField(max_length=100,default="title")
    model_name = models.CharField(max_length=6, choices=COLOR_CHOICES, default='Naive')
    field_name = models.TextField(default ="This is a default value")

    def __str__(self):
        return self.title

# Create your models here.
