from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api),
    path('api/<str:id>', views.api_RUD)
]
