"""
URL configuration for Gigi_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('library/detail/<int:pk>', views.detail_book, name='detail-book'),
    path('library/create/', views.create_book, name='create-book'),
    # path('library/update/<int:pk>', views.update_book, name='update-book'),
    # path('library/delete/<int:pk>', views.delete_book, name='delete-book'),
]
