from django.contrib import admin
from django.urls import path
from its_try import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index")
]

handle404 = 'its_try.views.error_404'