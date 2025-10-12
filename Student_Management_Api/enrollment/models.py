from django.db import models

# Create your models here.
class Enrollment(models.Model):
    # use 'students.Student' and 'courses.Course' strings to avoid import issues
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')  # prevents duplicate enrollments
        ordering = ['-enrolled_at']

    def __str__(self):
        return f"{self.student} -> {self.course}"
