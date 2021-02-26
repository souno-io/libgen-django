from django.db import models
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator, UserManager, AbstractBaseUser, \
    PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserProfile(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    id = models.AutoField(u'用户编号', primary_key=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    full_name = models.CharField(_('姓名'), max_length=60, null=False, blank=False, help_text='姓名')
    # depart_id = models.ForeignKey('Department', related_name='depart_id', verbose_name=u"部门", on_delete=models.CASCADE,null=True, help_text='所属部门')
    mobile = models.CharField(u'电话号码', max_length=20, unique=True, blank=True, null=True, default=None,
                              help_text='电话号码')
    sid_num = models.CharField(u'身份证号', max_length=18, unique=True, blank=True, null=True, default=None,
                               help_text='身份证号')
    is_doctor = models.BooleanField(u'是否医生', unique=False, blank=False, null=True, default=False, help_text='是否医生')
    role_code = models.IntegerField(u'角色代码', unique=False, blank=True, null=True, default=None, help_text='角色代码')
    email = models.EmailField('邮件地址', max_length=150, blank=True, help_text='用于登录验证的邮件地址')
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = u"员工信息"
        verbose_name_plural = verbose_name
