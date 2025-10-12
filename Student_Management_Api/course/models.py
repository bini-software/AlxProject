from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150)
    course_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.title}"
    