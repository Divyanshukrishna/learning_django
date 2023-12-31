from django.contrib import admin
from django.urls import path
from pp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index ,name="index"),
    path('base/',views.base, name="base"),
    path('page/',views.page, name="page")
]

handler404 = 'pp.views.error_404'