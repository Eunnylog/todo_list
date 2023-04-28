from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ListSerializer, ListCreateSerializer
from rest_framework.generics import get_object_or_404

# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = ListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
# 상세게시글     
class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ListSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            serializer = ListCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)
    
    
    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)