# ====================================
# > Project:No1_scilib
# > Model_name:adminx
# > Author:souno@qq.com
# > Datetime:2020/5/22 13:30
# >
# ======================================
import xadmin
from xadmin import views
from .models import SysConfigs

class SysConfigsAdmin(object):
    list_display = ['id', 'web_name', 'server_ip','server_port','addeddatetime']
    search_fields = ['id', 'web_name', 'server_ip','server_port','addeddatetime']
    list_filter = ['id', 'web_name', 'server_ip','server_port','addeddatetime']

xadmin.site.register(SysConfigs, SysConfigsAdmin)