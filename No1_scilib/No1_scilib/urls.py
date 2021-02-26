"""No1_scilib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
import xadmin
from website import views as web_views
from users import views as user_views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', xadmin.site.urls, name='admin'),
    path('sci/', include('website.urls')),
    path('sci/', include('configs.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-authtoken', obtain_jwt_token),
    path('', web_views.index, name='index'),
    path('down_reader/', web_views.down_reader, name='down_reader'),
    path('login/',user_views.login_view, name='login'),
    path('login_check/',user_views.login_check, name='login_check'),
    path('logout/',user_views.logout_view, name='logout'),
    path('epub/',web_views.epub_reader, name='epub')
    # path('docs/', include('rest_framework_docs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
