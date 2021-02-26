# django rest framework-过滤、搜索、排序

## 过滤DjangoFilterBackend：

默认情况下 DRF generic list view 会返回整个 `queryset`查询结果，但通常业务只是需要其中一部分，这种情况下就需要使用 "过滤器" 来限制返回结果集。
 最笨的方式是继承`GenericAPIView`类或使用继承了`GenericAPIView`的类，然后重写`.get_queryset()` 方法 ，首先我们看类视图中增加一个方法`get_queryset`



```python
from rest_framework import generics
class ArticleViewSet(generics.ListAPIView):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的

    def get_queryset(self):
        queryset = Article.objects.all()
        read_num = self.request.query_params.get('read_num', 0)  # 获取查询字段值
        if read_num:
            queryset = queryset.filter(read_num__gt=int(read_num))

        return queryset
```

###### 测试效果

1. 当传递的

   ```
   read_num=83
   ```

   按照方法

   ```
   get_queryset
   ```

   中判断条件找出大于

   ```
   83
   ```

   的有

   ```
   3
   ```

   条记录。

   ![img](https:////upload-images.jianshu.io/upload_images/9286065-736acc5e5d03e4e7.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

   image.png

2. 

   

   我们再试一试如果不传递，查出记录有7条记录。

   ![img](https:////upload-images.jianshu.io/upload_images/9286065-1b86548d132bb2e8.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

   image.png

###### 小结

上面我们通过重写`get_queryset`方法来达到过滤效果，这样做如果在过滤条件复杂的情况下，代码会显得过于冗余，而且有可能大部分代码一直在重复实现类似的功能，在日常操作中，我们需要获取指定条件的数据，例如对于文章，我们需要指定分类、浏览数、点赞数等。有时候我们需要按照浏览数进行排序。这些都需要我们对ArticleViewSet进行更多的拓展。

### 过滤OrderingFilter

REST framework提供了对于排序的支持，使用REST framework提供的OrderingFilter过滤器后端即可。OrderingFilter过滤器要使用ordering_fields 属性来指明可以进行排序的字段有哪些。



```python
from rest_framework.filters import OrderingFilter

    # 过滤器，只针对当前查询过滤，所以不在settings.py中配置
    filter_backends = (OrderingFilter,)
    # 排序
    ordering_fields = ('create_time', 'price', 'sales')
```

### 自定义过滤器django-filter模块

```
django-filter`库包括一个`DjangoFilterBackend`类，它支持`REST`框架的高度可定制的字段过滤。
 首先安装`django-filter
```



```swift
pip install django-filter
```

然后将`django_filters`添加到`Django`的`INSTALLED_APPS`。



```bash
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
```

或者将过滤器加到单个View或ViewSet中(**一般使用这种**)：



```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class ArticleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的
    # 过滤器
    filter_backends = (DjangoFilterBackend,)
    # 如果要允许对某些字段进行过滤，可以使用filter_fields属性。
    filter_fields = ('title', 'category')

    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     read_num = self.request.query_params.get('read_num', 0)
    #
    #     if read_num:
    #         queryset = queryset.filter(read_num__gt=int(read_num))
    #
    #     return queryset
```

###### 测试效果



![img](https:////upload-images.jianshu.io/upload_images/9286065-f3fe3d0eea1218e5.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image.png


 可以看出通过加过滤器和添加对应字段会过滤相关的，注意这里是精确匹配，字段间是且的关系，若一个为空，则按照其他的匹配，比如`title=测试&category=`则按照`title`来精确查找。



#### 自定义过滤类

默认是按照精准匹配，若想达到模糊搜索，可以自定义过滤类，再用filter_class指定过滤集合类。
 新建过滤文件`filters.py`



```python
from django_filters import rest_framework
from article.models import Article

class AriticleFilter(rest_framework.FilterSet):
    min_read = rest_framework.NumberFilter(field_name='read_num', lookup_expr='gte')
    max_read = rest_framework.NumberFilter(field_name='read_num', lookup_expr='lte')
    title = rest_framework.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'category', 'min_read', 'max_read']
```

将视图类修改



```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AriticleFilter

class ArticleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的
    # 过滤器
    filter_backends = (DjangoFilterBackend,)
    # 如果要允许对某些字段进行过滤，可以使用filter_fields属性。
    #filter_fields = ('title', 'category')
    # 使用自定义过滤器
    filter_class = AriticleFilter

    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     read_num = self.request.query_params.get('read_num', 0)
    #
    #     if read_num:
    #         queryset = queryset.filter(read_num__gt=int(read_num))
    #
    #     return queryset
```

测试效果：



![img](https:////upload-images.jianshu.io/upload_images/9286065-8f3b41c5851b014e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image.png

## 搜索SearchFilter

如果要明确指定可以对哪些字段进行搜索，可以使用search_fields属性，默认为可以对`serializer_class`属性指定的串行器上的任何可读字段进行搜索：



```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .filters import AriticleFilter

class ArticleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的
    # 过滤器
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    # 如果要允许对某些字段进行过滤，可以使用filter_fields属性。
    #filter_fields = ('title', 'category')
    # 使用自定义过滤器
    filter_class = AriticleFilter
    search_fields = ('title', 'description', 'content')
```

可以看出多了个搜索框



![img](https:////upload-images.jianshu.io/upload_images/9286065-90ec367f96a35b54.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image.png

默认情况下，搜索将使用不区分大小写的部分匹配。 搜索参数可以包含多个搜索项，它们应该是空格和/或逗号分隔。 如果使用多个搜索项，则仅当所有提供的条款匹配时，才会在列表中返回对象。默认情况下，搜索参数被命名为“search”，但这可能会被SEARCH_PARAM设置覆盖。
 The search behavior may be restricted by prepending various characters to the search_fields.
 可以通过在search_fields中加入一些字符来限制搜索行为，如下：
 '^'  ：以xx字符串开始搜索
 '='  ：完全匹配
 '@' ：全文搜索（目前只支持Django的MySQL后端）
 '$'  ：正则表达式搜索
 如：search_fields = ('@username', '=email')

## 排序

OrderingFilter 类支持对单个查询字段结果集进行排序。
 默认情况下，查询参数被命名为“ordering”，但这可能会被ORDERING_PARAM设置覆盖。
 可以使用ordering_fields属性明确指定可以对哪些字段执行排序，这有助于防止意外的数据泄露，例如允许用户对密码散列字段或其他敏感数据进行排序。
 如果不指定ordering_fields属性，则默认为可以对serializer_class属性指定的串行器上的任何可读字段进行过滤。



```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import AriticleFilter

class ArticleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()  # 查询结果集
    serializer_class = ArticleSerializer # 序列化类
    pagination_class = ArticlePagination   # 自定义分页会覆盖settings全局配置的
    # 过滤器 过滤，搜索，排序
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    # 如果要允许对某些字段进行过滤，可以使用filter_fields属性。
    #filter_fields = ('title', 'category')
    # 使用自定义过滤器
    filter_class = AriticleFilter
    # 搜索
    search_fields = ('title', 'description', 'content')
    # 排序
    ordering_fields = ('id', 'read_num')
```

效果：



![img](https:////upload-images.jianshu.io/upload_images/9286065-cb5c0d9e92cfa2a6.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image.png



作者：Python野路子
链接：https://www.jianshu.com/p/292a06275712
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。