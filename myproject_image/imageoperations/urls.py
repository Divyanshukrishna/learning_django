from django.contrib import admin
from django.urls import path,include
from imageoperations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.upload_image)
]