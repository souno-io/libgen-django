# ====================================
# > Project:No1_scilib
# > Model_name:urls
# > Author:souno@qq.com
# > Datetime:2020/5/22 11:51
# >
# ======================================

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import SysConfigsViewSet


api_root = routers.DefaultRouter()
api_root.register(r'configs', SysConfigsViewSet, basename='Configs-List')

urlpatterns = [
    path('api/', include(api_root.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)