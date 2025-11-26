from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('getAll/', views.get_all_students, name='get_all_students'),
    path('university/add/', views.add_university, name='add_university'),
    path('university/getAll/', views.get_all_universities, name='get_all_universities'),
]
