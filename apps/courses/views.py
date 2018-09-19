from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'index.html', context)

def process(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validations(request.POST)
        errors2 = Description.objects.basic_validations(request.POST)
        if len(errors) or len(errors2):
            for key, value in errors.items():
                messages.error(request, value)
            for key, value in errors2.items():
                messages.error(request, value)
        else:
            Description.objects.create(desc=request.POST['desc'])
            Course.objects.create(name=request.POST['course_name'], course_desc=Description.objects.last())
    return redirect('/')
        
def destroy(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'destroy.html', context)

def remove(request):
    if request.method == 'POST':
        remove = Course.objects.get(id=request.POST['id'])
        remove.delete()
    return redirect('/')

def comments(request,id):
    context = {
        "id": id,
        "comments": Comment.objects.filter(course_id=id)
    }
    return render(request, 'comments.html', context)

def add_comment(request):
    if request.method == 'POST':
        errors = Comment.objects.basic_validations(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Comment.objects.create(comment=request.POST['comment'], course=Course.objects.get(id=request.POST['id']))
    return redirect("/comments/" + str(request.POST['id']))
