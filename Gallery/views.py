from django.shortcuts import render

# Create your views here.

def gallery_view(request):
    return render(request,'Gallery/gallery.html')

def event_view(request):
    return render(request,'Gallery/event.html')