from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),

   
    path('correction/', views.course_list, name='course_list'),
    path('correction/<int:course_id>/', views.course_detail, name='course_detail'),  # Détails d'un cours
    path('correction/add/', views.add_course, name='add_course'),  # Ajout d'un cours
    path('correction/edit/<int:course_id>/', views.edit_course, name='edit_course'),  # Modification d'un cours
    path('correction/delete/<int:course_id>/', views.delete_course, name='delete_course'),  # Suppression d'un cours
    path('correction/edit_question/<int:question_id>/', views.edit_question, name='edit_question'),
    path('correction/edit_answer/<int:question_id>/', views.edit_answer, name='edit_answer'),
    path('correction/<int:course_id>/edit_summary/', views.edit_summary, name='edit_summary'),
    path('correction/delete_question/<int:question_id>/', views.delete_question, name='delete_question'),
    path('correction/<int:course_id>/download/', views.download_file, name='download_file'),
]
