# ====================================
# > Project:No1_scilib
# > Model_name:serializers
# > Author:souno@qq.com
# > Datetime:2020/5/22 11:52
# >
# ======================================

from .models import SysConfigs
from rest_framework import serializers


class SysConfigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysConfigs
        fields = "__all__"
        #depth = 2
