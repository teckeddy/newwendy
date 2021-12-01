from django.shortcuts import render
from . models import Gallery

# Create your views here.
def gallery(request):
    context=Gallery.objects.all()
    return render(request, "wendy/gallery.html",{"photos":context})