from django.contrib import admin
from .models import Question, GeneratedQuestion
admin.site.register(GeneratedQuestion)
admin.site.register(Question)
# Register your models here.
