from django.urls import path

from Gallery.views import gallery_view
from . import views

app_name="Gallery"

urlpatterns=[
    path('',gallery_view,name="gallery"),
]