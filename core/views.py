from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Image


class ImageListView(ListView):
    template_name = "index.html"
    model = Image
    context_object_name = "images"


class ImageCreateView(CreateView):
    model = Image
    template_name = 'create_image.html'
    success_url = '/'
    fields = ['title', 'image', 'description']

class ImageUpdateView(UpdateView):
    model = Image
    template_name = 'create_image.html'
    pk_url_kwarg = 'pk'
    success_url = '/'
    fields = ['title', 'description']

class ImageDeleteView(DeleteView):
    model = Image
    pk_url_kwarg = 'pk'
    template_name = 'image_confirm_delete.html'
    success_url = '/'
    success_message = "The topic has been successfully deleted"


class ImageDetailView(DetailView):
    model = Image
    context_object_name = "image"
    template_name = 'image_detail.html'
    success_url = '/'
    fields = ['title', 'image', 'description']

