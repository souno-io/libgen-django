import xadmin
from xadmin import views
from .models import NonFiction, Scimag, Fiction

class NonFictionAdmin(object):
    list_display = ['id', 'title', 'volumeinfo','series','authors','year','edition','publisher','format']
    search_fields = ['id', 'title', 'volumeinfo','series','authors','year','edition','publisher','format']
    list_filter = ['id', 'title', 'volumeinfo','series','authors','year','edition','publisher','format']


class ScimagAdmin(object):
    list_display = ['id', 'title', 'volume', 'authors','year','sizeinbytes', 'pubmedid','abstracturl']
    search_fields = ['id', 'title', 'volume', 'authors','year','sizeinbytes', 'pubmedid','abstracturl']
    list_filter = ['id', 'title', 'volume', 'authors','year','sizeinbytes', 'pubmedid','abstracturl']


class FictionAdmin(object):
    list_display = ['id', 'title', 'language', 'authorname1','year','role1', 'publisher','format']
    search_fields = ['id', 'title', 'language', 'authorname1','year','role1', 'publisher','format']
    list_filter = ['id', 'title', 'language', 'authorname1','year','role1', 'publisher','format']



class GlobalSettings(object):
    site_title = "操作后台"  # 页眉
    site_footer = "souno.cn"  # 页脚
    # menu_style = 'accordion'  # 左侧样式


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(NonFiction, NonFictionAdmin)
xadmin.site.register(Scimag, ScimagAdmin)
xadmin.site.register(Fiction, FictionAdmin)

