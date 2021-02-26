import xadmin
from xadmin import views
from .models import UserProfile
# from django.contrib.auth.admin import UserAdmin
from xadmin.plugins.auth import UserAdmin


class UsersAdmin(UserAdmin):
    list_display = ['id', 'username', 'full_name', 'email', 'date_joined', 'is_active', 'is_staff']
    search_fields = ['id', 'username', 'full_name', 'email', 'date_joined', 'is_active', 'is_staff']
    list_filter = ['id', 'username', 'full_name', 'email', 'date_joined', 'is_active', 'is_staff']


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UsersAdmin)
