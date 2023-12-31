from django.contrib import admin
from django.urls import path,include
from percent import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home")
]

handler404='percent.views.error_404'