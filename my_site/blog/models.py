from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    topic = models.CharField(max_length=200)
    difficulty_level = models.IntegerField()

    def __str__(self):
        return self.topic

class Schedule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    lesson_date = models.DateTimeField()

    def __str__(self):
        return f"{self.student.name} - {self.lesson.topic} on {self.lesson_date}"

class Competition(models.Model):
    participants = models.ManyToManyField(Student)
    date = models.DateTimeField()

    def __str__(self):
        return f"Competition on {self.date}"