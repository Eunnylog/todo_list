from rest_framework import serializers
from articles.models import Article

class ListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.name
    class Meta:
        model = Article
        fields = "__all__"


class ListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title","is_complete")