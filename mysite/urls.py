"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from conversation.views import convers
from personal.views import chat
from conversation.views import message_endpoint
from personal.views import get_names
from personal.views import home
from personal.views import search_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('item/<str:title>/', convers),
    path('message_endpoint/', message_endpoint),
    path('get_names/', get_names),
    path('chat/', chat, name='chat'),
    path('search_page/', search_page, name='search_page')

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)