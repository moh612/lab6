from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    courses = models.ManyToManyField(Course, related_name='students')