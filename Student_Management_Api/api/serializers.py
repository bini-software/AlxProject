from rest_framework import serializers
from student.models import Student
from course.models import Course
from enrollment.models import Enrollment



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), write_only=True, source='student')
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True, source='course')

    class Meta:
        model = Enrollment
        fields = '__all__'
