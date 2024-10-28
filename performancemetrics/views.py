from django.shortcuts import render
from .service.recommendation_engine import recommend_quizzes

# Create your views here.

def user_dashboard(request):
    user_id = request.user
    recommendations = recommend_quizzes(user_id)
    return render(request, 'pages/performance/index.html', {'recommendations': recommendations})
