from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from hitcount.views import HitCountDetailView

from qrproject import settings
from .models import Image
# for qrcode purpose
from PIL import Image as PILImage
from io import BytesIO
import qrcode
from django.core.files import File
import os


def generate_image_link(http_origin, id):
    return "/".join([os.path.dirname(http_origin), "image", str(id)])


def make_qrcode_image(image, text):
    im = PILImage.open(image)
    qr = qrcode.QRCode(box_size=3, border=2)
    qr.add_data(text)
    qr.make()
    img_qr = qr.make_image()
    pos = (im.size[0] - img_qr.size[0], im.size[1] - img_qr.size[1])
    im.paste(img_qr, pos)
    bytes_io = BytesIO()  # create a BytesIO object
    im.save(bytes_io, im.format)  # save image to BytesIO object
    return File(bytes_io, name=os.path.basename(image.name))  # create a django friendly File object


class ImageListView(ListView):
    template_name = "index.html"
    model = Image
    context_object_name = "images"


class ImageCreateView(CreateView):
    model = Image
    template_name = 'create_image.html'
    success_url = '/'
    fields = ['title', 'image', 'description']

    def form_valid(self, form):
        image = form.save(commit=True)
        url = generate_image_link(self.request.build_absolute_uri(), image.id)
        old_name = image.image.name
        image.image = make_qrcode_image(image.image, url)
        os.remove(os.path.join(settings.MEDIA_ROOT, old_name))
        image.save()
        return redirect('index')


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


class ImageDetailView(HitCountDetailView):
    model = Image
    context_object_name = "image"
    template_name = 'image_detail.html'
    success_url = '/'
    count_hit = True


class ImageDownload(DetailView):
    model = Image
    context_object_name = "image"
    fields = ['title', 'image']

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.download_count += 1
        obj.save()
        return HttpResponse(obj.download_count)

class ImageContact(DetailView):
    model = Image
    context_object_name = "image"
    fields = ['title', 'image']

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.contact_count += 1
        obj.save()
        return HttpResponse(obj.download_count)


