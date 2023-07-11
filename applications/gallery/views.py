from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator

from .models import GalleryImage


class GalleryView(generic.ListView):
    template_name = 'gallery/gallery.html'
    model = GalleryImage
    context_object_name = 'images'
    paginate_by = 10
    queryset = GalleryImage.objects.all()
