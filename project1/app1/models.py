from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.PositiveIntegerField(unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.rollno})"
# Create your models here.

