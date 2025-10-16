from django.shortcuts import render
from rest_framework import generics
from student.models import Student
from course.models import Course
from enrollment.models import Enrollment
from . import serializers

# Create your views here.
class StudentCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer



class CourseCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer



class EnrollmentCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer

class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer