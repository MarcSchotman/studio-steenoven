from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from main import settings
from .models import Image

def index(request):
    images = [img.image.url for img in Image.objects.all()]
    template = loader.get_template(f"image_gallery/index.html")
    context = {
        "images": images,
    }
    return HttpResponse(template.render(context, request))

