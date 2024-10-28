from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import include
# from .views import generate_course

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('', include('gestion.urls')),
]
