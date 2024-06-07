from django.contrib import admin
from .models import * #Post, Student, Lesson, Schedule, Competition

admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Schedule)
admin.site.register(Competition)

# Register your models here.
