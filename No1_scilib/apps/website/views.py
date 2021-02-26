from django.shortcuts import render
from rest_framework import viewsets
from .models import NonFiction, Scimag, Fiction
from configs.models import SysConfigs
from .serializers import NonFictionSerializer, ScimagSerializer, FictionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filter import NonFictionFilter, ScimagFilter, FictionFilter
from .pagination import NonFictionPagination, ScimagPagination, FictionPagination
from django.contrib.auth.decorators import login_required


class NonFictionViewSet(viewsets.ModelViewSet):
    """
    get:
        默认返回所有的非文学作品信息，使用?search=''对应搜索，字段=''过滤。
    put:
        更新一条项目。
    patch:
        更新一条项目。
    delete:
        删除一条项目。
    """
    queryset = NonFiction.objects.all()
    serializer_class = NonFictionSerializer
    pagination_class = NonFictionPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filterset_class = NonFictionFilter
    # filter_fields = ('authors', 'publisher', 'year', 'language', 'format', 'series',)
    search_fields = ('title', 'authors', 'publisher', 'format', 'language',)

    # def get_queryset(self):
    #     queryset = NonFiction.objects.all()
    #     return queryset


class ScimagViewSet(viewsets.ModelViewSet):
    """
    get:
        默认返回所有的非文学作品信息，使用?search=''对应搜索，字段=''过滤。
    put:
        更新一条项目。
    patch:
        更新一条项目。
    delete:
        删除一条项目。
    """
    queryset = Scimag.objects.all()
    serializer_class = ScimagSerializer
    pagination_class = ScimagPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = ScimagFilter
    # filter_fields = ('authors', 'publisher', 'year', 'language', 'format', 'series',)
    search_fields = ('title', 'authors')

    # def get_queryset(self):
    #     queryset = NonFiction.objects.all()
    #     return queryset


class FictionViewSet(viewsets.ModelViewSet):
    """
    get:
        默认返回所有的非文学作品信息，使用?search=''对应搜索，字段=''过滤。
    put:
        更新一条项目。
    patch:
        更新一条项目。
    delete:
        删除一条项目。
    """
    queryset = Fiction.objects.all()
    serializer_class = FictionSerializer
    pagination_class = FictionPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = FictionFilter
    # filter_fields = ('authors', 'publisher', 'year', 'language', 'format', 'series',)
    search_fields = ('title', 'authorname1')

    # def get_queryset(self):
    #     queryset = NonFiction.objects.all()
    #     return queryset


# @login_required
def index(request):
    conf = SysConfigs.objects.get(id=1)
    return render(request, 'index.html',
                  {'web_name': conf.web_name, 'server_ip': conf.server_ip, 'server_port': conf.server_port,
                   'web_desc': conf.web_desc, 'web_foot': conf.web_foot})


# def index(request):
#     if request.user.is_authenticated():
#         username = request.user.username
#         print(dir(request.user))
#         return render(request, 'index.html', {'username': username})
#     else:
#         username = '游客'
#         return render(request, 'index.html', {'username': username})


def down_reader(request):
    conf = SysConfigs.objects.get(id=1)
    return render(request, 'download_reader.html', {'web_name': conf.web_name, 'web_foot': conf.web_foot})


def epub_reader(request):
    return render(request, 'epub-reader.html')
