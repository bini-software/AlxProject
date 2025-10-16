from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150)
    course_code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"
    