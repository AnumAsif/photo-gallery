from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, categories, Location

# Create your views here.
def index(request):
    images = Image.get_images
    img_categories = categories.get_categories
    locations = Location.get_location
    return render(request, 'index.html', {"images":images, "categories":img_categories, "locations":locations})

def gallery(request,category_id):
    
    images = Image.search_image(category_id)
    img_categories = categories.get_categories
    return render(request,'gallery.html',{'images':images,"categories":img_categories})

def gallery_by_location(request, location):
    images =Image.search_image_by_location(location)
    return render(request,'gallery.html',{'images':images})    

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.get_image_by_category(search_term)
        category = search_term

        return render(request, 'search.html',{"category":category,"images": searched_images})

    else:
        category = "You haven't searched for any category"
        return render(request, 'search.html',{"category":category})