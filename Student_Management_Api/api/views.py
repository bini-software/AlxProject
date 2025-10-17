from django.shortcuts import render
<<<<<<< HEAD
from rest_framework import generics
=======

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
>>>>>>> main
from student.models import Student
from course.models import Course
from enrollment.models import Enrollment
from . import serializers

<<<<<<< HEAD
# Create your views here.
class StudentCreateView(generics.ListCreateAPIView):
=======
class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentCreateView(generics.CreateAPIView):
>>>>>>> main
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer


<<<<<<< HEAD

class CourseCreateView(generics.ListCreateAPIView):
=======
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CourseCreateView(generics.CreateAPIView):
>>>>>>> main
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


<<<<<<< HEAD

class EnrollmentCreateView(generics.ListCreateAPIView):
=======
class EnrollmentListView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer

class EnrollmentCreateView(generics.CreateAPIView):
>>>>>>> main
    queryset = Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer

class EnrollmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer