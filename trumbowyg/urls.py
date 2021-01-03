# coding=utf-8
from django.urls import path

from trumbowyg.views import upload_image


urlpatterns = [
   path('upload_image/', upload_image, name='trumbowyg_upload_image'),
]
