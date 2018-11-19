"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('article/', include('articles.urls', namespace='articles')),
    path('search/', include('search.urls', namespace='search')),
    path('addpost/', include('addpost.urls', namespace='addpost')),
    path('redactors/', include('redactors.urls', namespace='redactors')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('supermanagerlogin/', auth_views.login,  {'template_name': 'login/login.html'}),
    path('about/', TemplateView.as_view(template_name="about/about.html"), name='about'),
    path('logout/', auth_views.logout, {"next_page" : "/"}, name='logout'),
    path('supermanageradmin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
