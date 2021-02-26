from rest_framework import generics
from django_filters import rest_framework as filters
from .models import NonFiction, Scimag, Fiction


class NonFictionFilter(filters.FilterSet):
    language = filters.CharFilter(field_name='language', lookup_expr='icontains')
    formats = filters.CharFilter(field_name='format', lookup_expr='icontains')  # 等价于 sql 中的 like； i 表示忽略大小写
    #min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = NonFiction
        fields = ['authors', 'publisher', 'year', 'language', 'series']


class ScimagFilter(filters.FilterSet):
    #language = filters.CharFilter(field_name='language', lookup_expr='icontains')  # 等价于 sql 中的 like； i 表示忽略大小写
    #min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Scimag
        fields = ['authors', 'year', 'title']


class FictionFilter(filters.FilterSet):
    #language = filters.CharFilter(field_name='language', lookup_expr='icontains')  # 等价于 sql 中的 like； i 表示忽略大小写
    #min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    #max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Fiction
        fields = ['authorname1', 'year', 'title']
