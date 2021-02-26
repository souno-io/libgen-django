from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import NonFictionViewSet, ScimagViewSet, FictionViewSet


api_root = routers.DefaultRouter()
api_root.register(r'nonfiction', NonFictionViewSet, basename='nonfiction-List')
api_root.register(r'scimag', ScimagViewSet, basename='scimag-List')
api_root.register(r'fiction', FictionViewSet, basename='fiction-List')

urlpatterns = [
    path('api/', include(api_root.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)