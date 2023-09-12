from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api),
    path('api/<int:id>', views.api_RUD)
]
