from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [

    path('student/', views.StudentCreateView.as_view()),
    path('student/<int:pk>/', views.StudentDetailView.as_view()),

    path('course/', views.CourseCreateView.as_view()),
    path('course/<int:pk>/', views.CourseDetailView.as_view()),

    path('enrollment/', views.EnrollmentCreateView.as_view()),
    path('enrollment/<int:pk>/', views.EnrollmentDetailView.as_view())
]