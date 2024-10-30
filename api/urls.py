from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("product/((?P<pk>\d+)/)?", csrf_exempt(ProductView.as_view())),
	  path('content/', include('content.urls')),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]