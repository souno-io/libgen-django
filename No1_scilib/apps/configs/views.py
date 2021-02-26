from django.shortcuts import render
from rest_framework import viewsets
from .models import SysConfigs
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import SysConfigsSerializer


class SysConfigsViewSet(viewsets.ModelViewSet):
    queryset = SysConfigs.objects.all()
    serializer_class = SysConfigsSerializer
    # filter_fields = ('authors', 'publisher', 'year', 'language', 'format', 'series',)
