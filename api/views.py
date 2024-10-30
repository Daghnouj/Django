from http import HTTPStatus
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, get_object_or_404


from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question

from django.http import HttpResponse, FileResponse, Http404
import mimetypes

from api.serializers import *


try:

    from home.models import Product

except:
    pass

class ProductView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        serializer.save()
        return Response(data={
            'message': 'Record Created.',
            'success': True
        }, status=HTTPStatus.OK)

    def get(self, request, pk=None):
        if not pk:
            return Response({
                'data': [ProductSerializer(instance=obj).data for obj in Product.objects.all()],
                'success': True
            }, status=HTTPStatus.OK)
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        return Response({
            'data': ProductSerializer(instance=obj).data,
            'success': True
        }, status=HTTPStatus.OK)

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        serializer = ProductSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        serializer.save()
        return Response(data={
            'message': 'Record Updated.',
            'success': True
        }, status=HTTPStatus.OK)

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        obj.delete()
        return Response(data={
            'message': 'Record Deleted.',
            'success': True
        }, status=HTTPStatus.OK)

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = course.questions.all()  # Récupère les questions associées

    return render(request, 'content/course_detail.html', {'course': course, 'questions': questions})



def add_course(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        language = request.POST.get('language')
        image = request.FILES.get('image')
        file = request.FILES.get('file')
        # Créer un nouvel objet Course
        course = Course(title=title, description=description, language=language,image=image, file=file)
        course.save()

        # Générer des questions
        questions = course.process_file()

        # Rediriger vers la page de détails du cours ou afficher les questions
        return render(request, 'content/course_detail.html', {'course': course, 'questions': questions})

    return render(request, 'content/add_course.html')



def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.title = request.POST['title']
        course.description = request.POST['description']
        course.save()
        return redirect('course_detail', course_id=course.id)
    return render(request, 'content/edit_course.html', {'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'content/delete_course.html', {'course': course})

def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        question.text = request.POST.get('text', question.text)
        question.save()
        return redirect('course_detail', course_id=question.course.id)
    return HttpResponse(status=405)

def edit_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        question.answer = request.POST.get('answer', question.answer)
        question.save()
        return redirect('course_detail', course_id=question.course.id)
    return HttpResponse(status=405)

def edit_summary(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.summary = request.POST.get('summary', course.summary)
        course.save()
        return redirect('course_detail', course_id=course.id)
    return HttpResponse(status=405)

def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        course_id = question.course.id
        question.delete()
        return redirect('course_detail', course_id=course_id)
    return HttpResponse(status=405)

def download_file(request, course_id):
    # Charger le cours et vérifier si le fichier existe
    course = get_object_or_404(Course, id=course_id)
    if not course.file:
        raise Http404("File does not exist")

    # Détecter le type MIME du fichier
    mime_type, _ = mimetypes.guess_type(course.file.path)

    # Créer une réponse de fichier
    response = FileResponse(open(course.file.path, 'rb'), content_type=mime_type)
    response['Content-Disposition'] = f'attachment; filename="{course.file.name}"'
    
    return response

def home(request):
    return render(request, 'content/home.html') 