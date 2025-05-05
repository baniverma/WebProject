"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# from django.urls import path
#  # adjust if your views are in another app
# from myproject import views  # ✅ replace 'mainapp' with your real app name


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('index2/', views.index2, name='index2'),
#     path('nutrition/', views.nutrition, name='nutrition'),
#     path('recipe/', views.recipe, name='recipe'),
#     path('register/', views.register, name='register'),
#     path('review/', views.review, name='review'),
# ]
from django.urls import path
from core import views  # 👈 replace 'recipes' with your actual app name

urlpatterns = [
    path('', views.index, name='index'),
   
    path('index2/', views.index2, name='index2'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('register/', views.register, name='register'),
    path('review/', views.review, name='review'),
    path('recipe/', views.recipe, name='recipe'),
    path('calories/', views.calories, name='calories'),
    

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

