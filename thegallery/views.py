from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, categories

# Create your views here.
def gallery(request):
    images = Image.get_images
    img_categories = categories.get_categories
    return render(request, 'index.html', {"images":images, "categories":img_categories})