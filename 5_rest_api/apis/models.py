from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class School(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    grade = models.IntegerField()
    section = models.CharField(max_length=1)
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade}/{self.section}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)
    def slug(self):
        return f"{self.first_name.lower()}-{self.last_name.lower()}"  
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
