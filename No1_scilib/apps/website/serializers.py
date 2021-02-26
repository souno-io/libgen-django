from .models import NonFiction,Scimag,Fiction
from rest_framework import serializers


class NonFictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonFiction
        fields = "__all__"
        #depth = 2


class ScimagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scimag
        fields = "__all__"
        #depth = 2


class FictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiction
        fields = "__all__"
        #depth = 2