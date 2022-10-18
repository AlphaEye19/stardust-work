from django.urls import path

from Gallery.views import event_view, gallery_view
from . import views

app_name="Gallery"

urlpatterns=[
    path('',gallery_view,name="gallery"),
    path('events',event_view,name="event"),
]