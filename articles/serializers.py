from rest_framework import serializers
from articles.models import Article

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title",)