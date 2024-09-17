"""
URL configuration for Find_My_Way project.

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
from API import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('Jobs',views.JobsView,basename='Jobs')
router.register('Applications',views.ApplicationsView,basename='Applications')
router.register('Saved Jobs',views.SaveMyJobView,basename='Saved Jobs')
router.register('users',views.UserView,basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
]+router.urls
