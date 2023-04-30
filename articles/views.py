
from datetime import timezone, datetime
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
        if request.user == article.user:  # 작성자 확인
            serializer = ListCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                is_complete = serializer.validated_data.get('is_complete')  # 유효성 검사를 마친 후에 나온 데이터 중 is_complete
                if is_complete:  # 완료했으면
                    article.is_complete = True
                    article.completion_at = datetime.now()  # 완료한 시간으로 출력
                else:
                    article.is_complete = False  # 아직 완료하지 못했다면
                    article.completion_at = None 
                
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)
    
    
    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:  # 작성자 확인
            article.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)