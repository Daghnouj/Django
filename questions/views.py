from django.shortcuts import render

# Create your views here.

def indexQuestions(request):
    return render(request, 'pages/questions/index.html')
