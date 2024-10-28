from django.urls import path
from . import views
from .views import  search_courses, liste_cours, generate_course

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('cours/', liste_cours, name='liste_cours'),
    path('ajouter_cours/', views.ajouter_cours, name='ajouter_cours'),
    path('cours/<int:id>/modifier/', views.modifier_cours, name='modifier_cours'),
    path('cours/<int:id>/supprimer/', views.supprimer_cours, name='supprimer_cours'),
    path('cours/<int:id>/', views.details_cours, name='details_cours'),
    # path('cours/generate/<str:title>', ai_generate_courses, name='generarte'),
    path('cours/search/', search_courses, name='search_courses'),
    path('cours/generate/', generate_course, name='generate_course'),
    

    
]
# Ajout pour servir des fichiers média si en mode DEBUG


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
