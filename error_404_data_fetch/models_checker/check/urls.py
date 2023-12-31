from django.contrib import admin
from django.urls import path,include
from check import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),

]

handler404 = 'check.views.error_404'